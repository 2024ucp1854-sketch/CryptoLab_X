import os
import sys

# Allow importing files from the same src directory.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shift_cipher import encrypt, decrypt
from brute_force_dictionary import (
    load_dictionary,
    brute_force_dictionary
)
from chi_square_attack import chi_square_attack


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DICTIONARY_PATH = os.path.join(
    BASE_DIR,
    "dictionary",
    "english_words.txt"
)


def print_line():
    print("=" * 75)


def run_attack(ciphertext, actual_key, dictionary):

    print_line()
    print("CIPHERTEXT")
    print(ciphertext)

    print_line()
    print("ACTUAL KEY")
    print(actual_key)

    # -----------------------------
    # Dictionary Attack
    # -----------------------------

    dictionary_best, dictionary_results = (
        brute_force_dictionary(
            ciphertext,
            dictionary
        )
    )

    print_line()
    print("DICTIONARY SCORING ATTACK")

    print(
        "Predicted Key :",
        dictionary_best["key"]
    )

    print(
        "Plaintext     :",
        dictionary_best["plaintext"]
    )

    print(
        "Dictionary Score:",
        dictionary_best["score"]
    )

    dictionary_correct = (
        dictionary_best["key"] == actual_key
    )

    print(
        "Correct       :",
        "YES" if dictionary_correct else "NO"
    )

    # -----------------------------
    # Chi-Square Attack
    # -----------------------------

    chi_best, chi_results = chi_square_attack(
        ciphertext
    )

    print_line()
    print("CHI-SQUARE ATTACK")

    print(
        "Predicted Key :",
        chi_best["key"]
    )

    print(
        "Plaintext     :",
        chi_best["plaintext"]
    )

    print(
        "Chi-Square    :",
        f"{chi_best['score']:.4f}"
    )

    chi_correct = (
        chi_best["key"] == actual_key
    )

    print(
        "Correct       :",
        "YES" if chi_correct else "NO"
    )

    return (
        dictionary_best["key"],
        chi_best["key"],
        dictionary_correct,
        chi_correct
    )


def main():

    print("\n")
    print_line()
    print(" SHIFT CIPHER CRYPTANALYSIS ")
    print(" Brute Force + Dictionary + Chi-Square ")
    print_line()

    # Load dictionary.
    dictionary = load_dictionary(
        DICTIONARY_PATH
    )

    if not dictionary:
        print(
            "\nWARNING: Dictionary is empty!"
        )

        print(
            "Please add English words to:"
        )

        print(DICTIONARY_PATH)

    # ---------------------------------
    # Test Cases
    # ---------------------------------

    test_cases = [
        {
            "plaintext":
                "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
            "key": 3
        },

        {
            "plaintext":
                "THIS IS A SIMPLE TEST OF THE SHIFT CIPHER",
            "key": 7
        },

        {
            "plaintext":
                "CRYPTOGRAPHY PROVIDES METHODS FOR SECURE COMMUNICATION",
            "key": 12
        },

        {
            "plaintext":
                "COMPUTER SCIENCE IS AN INTERESTING SUBJECT",
            "key": 18
        },

        {
            "plaintext":
                "THE MESSAGE SHOULD BE EASY TO UNDERSTAND",
            "key": 22
        }
    ]

    results_table = []

    # ---------------------------------
    # Run all test cases
    # ---------------------------------

    for i, test in enumerate(
        test_cases,
        start=1
    ):

        plaintext = test["plaintext"]
        actual_key = test["key"]

        ciphertext = encrypt(
            plaintext,
            actual_key
        )

        print("\n")
        print(f"TEST CASE {i}")

        (
            dictionary_key,
            chi_key,
            dictionary_correct,
            chi_correct
        ) = run_attack(
            ciphertext,
            actual_key,
            dictionary
        )

        results_table.append({
            "test_case": i,
            "actual_key": actual_key,
            "dictionary_key": dictionary_key,
            "chi_square_key": chi_key,
            "dictionary_correct":
                dictionary_correct,
            "chi_square_correct":
                chi_correct
        })

    # ---------------------------------
    # Final Results Table
    # ---------------------------------

    print("\n\n")
    print_line()
    print("FINAL RESULTS")
    print_line()

    print(
        f"{'Test':<8}"
        f"{'Actual':<10}"
        f"{'Dictionary':<13}"
        f"{'Chi-Square':<13}"
        f"{'Dict?':<10}"
        f"{'Chi?':<10}"
    )

    print("-" * 75)

    for result in results_table:

        print(
            f"{result['test_case']:<8}"
            f"{result['actual_key']:<10}"
            f"{result['dictionary_key']:<13}"
            f"{result['chi_square_key']:<13}"
            f"{'YES' if result['dictionary_correct'] else 'NO':<10}"
            f"{'YES' if result['chi_square_correct'] else 'NO':<10}"
        )

    print_line()

    # ---------------------------------
    # Accuracy
    # ---------------------------------

    total = len(results_table)

    dictionary_accuracy = (
        sum(
            r["dictionary_correct"]
            for r in results_table
        )
        / total
        * 100
    )

    chi_accuracy = (
        sum(
            r["chi_square_correct"]
            for r in results_table
        )
        / total
        * 100
    )

    print(
        "\nDictionary Accuracy :",
        f"{dictionary_accuracy:.2f}%"
    )

    print(
        "Chi-Square Accuracy  :",
        f"{chi_accuracy:.2f}%"
    )

    print_line()


if __name__ == "__main__":
    main()
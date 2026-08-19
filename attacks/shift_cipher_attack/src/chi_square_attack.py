import string

from shift_cipher import decrypt


# Standard English letter frequencies in percentage.
ENGLISH_FREQUENCY = {
    'A': 8.167,
    'B': 1.492,
    'C': 2.782,
    'D': 4.253,
    'E': 12.702,
    'F': 2.228,
    'G': 2.015,
    'H': 6.094,
    'I': 6.966,
    'J': 0.153,
    'K': 0.772,
    'L': 4.025,
    'M': 2.406,
    'N': 6.749,
    'O': 7.507,
    'P': 1.929,
    'Q': 0.095,
    'R': 5.987,
    'S': 6.327,
    'T': 9.056,
    'U': 2.758,
    'V': 0.978,
    'W': 2.360,
    'X': 0.150,
    'Y': 1.974,
    'Z': 0.074
}


def count_letters(text):
    """
    Count occurrences of A-Z in the text.
    """
    counts = {letter: 0 for letter in string.ascii_uppercase}

    for char in text.upper():
        if char in counts:
            counts[char] += 1

    return counts


def chi_square_score(text):
    """
    Calculate Chi-Square statistic between
    observed text frequencies and expected
    English frequencies.
    """

    counts = count_letters(text)

    total_letters = sum(counts.values())

    if total_letters == 0:
        return float("inf")

    chi_square = 0.0

    for letter in string.ascii_uppercase:

        observed = counts[letter]

        expected = (
            ENGLISH_FREQUENCY[letter] / 100
        ) * total_letters

        if expected > 0:
            chi_square += (
                (observed - expected) ** 2
            ) / expected

    return chi_square


def chi_square_attack(ciphertext):
    """
    Try all 26 possible keys.

    The key with the smallest Chi-Square
    score is selected.
    """

    results = []

    for key in range(26):

        plaintext = decrypt(ciphertext, key)

        score = chi_square_score(plaintext)

        results.append({
            "key": key,
            "plaintext": plaintext,
            "score": score
        })

    # Smaller Chi-Square value = better match.
    best_result = min(
        results,
        key=lambda x: x["score"]
    )

    return best_result, results


if __name__ == "__main__":

    ciphertext = "KHOOR ZRUOG"

    best, results = chi_square_attack(ciphertext)

    print("\n===== CHI-SQUARE ATTACK =====")

    for result in results:
        print(
            f"Key = {result['key']:2d} | "
            f"Chi-Square = {result['score']:.4f} | "
            f"{result['plaintext']}"
        )

    print("\nBest Result")
    print("Key       :", best["key"])
    print("Plaintext :", best["plaintext"])
    print("Chi-Square:", f"{best['score']:.4f}")
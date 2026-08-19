import os
import re

from shift_cipher import decrypt


def load_dictionary(dictionary_path):
    words = set()

    if not os.path.exists(dictionary_path):
        print("Dictionary file not found:", dictionary_path)
        return words

    with open(dictionary_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()

            if word:
                words.add(word)

    return words


def tokenize(text):
    return re.findall(r"[a-zA-Z]+", text.lower())


def dictionary_score(text, dictionary):
    """
    Calculate dictionary score.
    Longer recognized English words get higher scores.
    """

    words = tokenize(text)

    if not words:
        return 0

    score = 0

    for word in words:
        if word in dictionary:
            score += len(word)

    return score


def brute_force_dictionary(ciphertext, dictionary):

    results = []

    for key in range(26):

        plaintext = decrypt(ciphertext, key)

        score = dictionary_score(
            plaintext,
            dictionary
        )

        results.append({
            "key": key,
            "plaintext": plaintext,
            "score": score
        })

    best_result = max(
        results,
        key=lambda x: x["score"]
    )

    return best_result, results
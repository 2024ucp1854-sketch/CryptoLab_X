import re
from collections import Counter


# English letter frequencies
ENGLISH_FREQ = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
    0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
    0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
    0.00074
]


# --------------------------------------------------
# 1. Clean ciphertext
# --------------------------------------------------
def clean_ciphertext(ciphertext):
    return re.sub(r'[^A-Za-z]', '', ciphertext).upper()


# --------------------------------------------------
# 2. Find repeated patterns
# --------------------------------------------------
def find_repeated_patterns(ciphertext, min_len=3, max_len=5):
    patterns = {}

    for length in range(min_len, max_len + 1):
        occurrences = {}

        for i in range(len(ciphertext) - length + 1):
            pattern = ciphertext[i:i + length]

            if pattern not in occurrences:
                occurrences[pattern] = []

            occurrences[pattern].append(i)

        for pattern, positions in occurrences.items():
            if len(positions) > 1:
                patterns[pattern] = positions

    return patterns


# --------------------------------------------------
# 3. Calculate distances
# --------------------------------------------------
def calculate_distances(patterns):
    distances = {}

    for pattern, positions in patterns.items():
        pattern_distances = []

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                distance = positions[j] - positions[i]
                pattern_distances.append(distance)

        distances[pattern] = pattern_distances

    return distances


# --------------------------------------------------
# 4. Find factors
# --------------------------------------------------
def find_factors(distances, max_key_length=20):
    factor_count = Counter()

    for distance_list in distances.values():

        for distance in distance_list:

            for factor in range(2, max_key_length + 1):

                if distance % factor == 0:
                    factor_count[factor] += 1

    return factor_count


# --------------------------------------------------
# 5. Kasiski analysis
# --------------------------------------------------
def kasiski_analysis(ciphertext):
    patterns = find_repeated_patterns(ciphertext)
    distances = calculate_distances(patterns)
    factors = find_factors(distances)

    print("\n========== KASISKI EXAMINATION ==========")

    print("\nRepeated Patterns:")

    for pattern, positions in patterns.items():
        print(f"{pattern}: {positions}")

    print("\nDistances:")

    for pattern, distance_list in distances.items():
        print(f"{pattern}: {distance_list}")

    print("\nFactor Frequency:")

    for factor, count in factors.most_common():
        print(f"Key Length {factor}: {count} occurrences")

    if not factors:
        return None

    # Select the factor having the highest occurrence
    estimated_length = factors.most_common(1)[0][0]

    return estimated_length


# --------------------------------------------------
# 6. Calculate Index of Coincidence
# --------------------------------------------------
def calculate_ic(text):
    n = len(text)

    if n <= 1:
        return 0.0

    counts = Counter(text)

    numerator = 0

    for count in counts.values():
        numerator += count * (count - 1)

    denominator = n * (n - 1)

    return numerator / denominator


# --------------------------------------------------
# 7. Split ciphertext into groups
# --------------------------------------------------
def split_into_groups(ciphertext, key_length):
    groups = []

    for i in range(key_length):
        groups.append(ciphertext[i::key_length])

    return groups


# --------------------------------------------------
# 8. Frequency analysis
# --------------------------------------------------
def frequency_analysis(group):
    counts = Counter(group)

    table = []

    for i in range(26):

        letter = chr(65 + i)
        count = counts.get(letter, 0)

        percentage = (count / len(group)) * 100

        table.append(
            (letter, count, percentage)
        )

    return table


# --------------------------------------------------
# 9. Find Caesar shift using Chi-Square
# --------------------------------------------------
def find_shift(group):

    n = len(group)
    counts = Counter(group)

    best_shift = 0
    best_score = float("inf")

    for shift in range(26):

        chi_square = 0

        for plaintext_index in range(26):

            cipher_index = (plaintext_index + shift) % 26

            cipher_letter = chr(65 + cipher_index)

            observed = counts.get(cipher_letter, 0)

            expected = n * ENGLISH_FREQ[plaintext_index]

            if expected > 0:

                chi_square += (
                    (observed - expected) ** 2
                ) / expected

        if chi_square < best_score:

            best_score = chi_square
            best_shift = shift

    return best_shift, best_score


# --------------------------------------------------
# 10. Find probable key
# --------------------------------------------------
def find_key(groups):

    key = ""

    print("\n========== FREQUENCY ANALYSIS ==========")

    for i, group in enumerate(groups):

        print(f"\nGroup {i + 1}")
        print("-" * 45)

        print("Ciphertext Group:", group)
        print("IC:", round(calculate_ic(group), 4))

        print("\nFrequency Table:")
        print("Letter\tCount\tPercentage")

        table = frequency_analysis(group)

        for letter, count, percentage in table:

            print(
                f"{letter}\t{count}\t{percentage:.2f}%"
            )

        shift, score = find_shift(group)

        key_letter = chr(65 + shift)

        print("\nProbable Shift:", shift)
        print("Probable Key Letter:", key_letter)
        print("Chi-Square:", round(score, 4))

        key += key_letter

    return key


# --------------------------------------------------
# 11. Vigenere Decryption
# --------------------------------------------------
def vigenere_decrypt(ciphertext, key):

    plaintext = ""

    for i, character in enumerate(ciphertext):

        cipher_value = ord(character) - ord('A')

        key_value = ord(
            key[i % len(key)]
        ) - ord('A')

        plain_value = (
            cipher_value - key_value
        ) % 26

        plaintext += chr(
            plain_value + ord('A')
        )

    return plaintext


# --------------------------------------------------
# 12. Vigenere Encryption
# --------------------------------------------------
def vigenere_encrypt(plaintext, key):

    ciphertext = ""

    for i, character in enumerate(plaintext):

        plain_value = ord(character) - ord('A')

        key_value = ord(
            key[i % len(key)]
        ) - ord('A')

        cipher_value = (
            plain_value + key_value
        ) % 26

        ciphertext += chr(
            cipher_value + ord('A')
        )

    return ciphertext


# --------------------------------------------------
# 13. Verify
# --------------------------------------------------
def verify(original_ciphertext, encrypted_ciphertext):

    return original_ciphertext == encrypted_ciphertext
    
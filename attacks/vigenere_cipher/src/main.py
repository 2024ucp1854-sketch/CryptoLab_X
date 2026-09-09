from vigenere_kasiski import (
    clean_ciphertext,
    kasiski_analysis,
    calculate_ic,
    split_into_groups,
    find_key,
    vigenere_decrypt,
    vigenere_encrypt,
    verify
)


# --------------------------------------------------
# Read ciphertext from input.txt
# --------------------------------------------------
def read_input(filename):

    with open(filename, "r") as file:
        return file.read()


# --------------------------------------------------
# Main Program
# --------------------------------------------------
def main():

    print("=" * 60)
    print(" VIGENERE CIPHER CRYPTANALYSIS")
    print(" KASISKI EXAMINATION AND FREQUENCY ANALYSIS")
    print("=" * 60)

    # Read input file
    ciphertext = read_input("../input.txt")

    # Clean ciphertext
    ciphertext = clean_ciphertext(ciphertext)

    print("\n========== INPUT ==========")

    print("Ciphertext Length:", len(ciphertext))

    print("Ciphertext:")
    print(ciphertext)

    # --------------------------------------------------
    # Kasiski Analysis
    # --------------------------------------------------

    key_length = kasiski_analysis(ciphertext)

    if key_length is None:

        print("\nUnable to determine key length.")

        return

    print("\n========== KEY LENGTH ==========")

    print("Estimated Key Length:", key_length)

    # --------------------------------------------------
    # Calculate groups
    # --------------------------------------------------

    groups = split_into_groups(
        ciphertext,
        key_length
    )

    print("\n========== GROUPS ==========")

    for i, group in enumerate(groups):

        print(
            f"Group {i + 1}: {group}"
        )

        print(
            f"IC: {calculate_ic(group):.4f}"
        )

    # --------------------------------------------------
    # Find key
    # --------------------------------------------------

    key = find_key(groups)

    print("\n========== RECOVERED KEY ==========")

    print("Key:", key)

    # --------------------------------------------------
    # Decrypt
    # --------------------------------------------------

    plaintext = vigenere_decrypt(
        ciphertext,
        key
    )

    print("\n========== RECOVERED PLAINTEXT ==========")

    print(plaintext)

    # --------------------------------------------------
    # Re-encrypt for verification
    # --------------------------------------------------

    encrypted = vigenere_encrypt(
        plaintext,
        key
    )

    print("\n========== VERIFICATION ==========")

    print(
        "Original Ciphertext Length:",
        len(ciphertext)
    )

    print(
        "Re-encrypted Ciphertext Length:",
        len(encrypted)
    )

    result = verify(
        ciphertext,
        encrypted
    )

    print(
        "Re-encryption matches original:",
        result
    )

    if result:

        print(
            "\nVerification Successful!"
        )

    else:

        print(
            "\nVerification Failed!"
        )


# --------------------------------------------------
# Program Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    main()
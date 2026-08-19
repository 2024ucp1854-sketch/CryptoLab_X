import string

ALPHABET = string.ascii_uppercase


def encrypt(text, key):
    """
    Encrypt text using Shift/Caesar Cipher.

    key: integer from 0 to 25
    """
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                index = ord(char) - ord('A')
                new_index = (index + key) % 26
                result += chr(ord('A') + new_index)

            else:
                index = ord(char) - ord('a')
                new_index = (index + key) % 26
                result += chr(ord('a') + new_index)

        else:
            result += char

    return result


def decrypt(text, key):
    """
    Decrypt text using Shift/Caesar Cipher.
    """
    return encrypt(text, -key)


if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    key = 3

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("Plaintext :", plaintext)
    print("Key       :", key)
    print("Ciphertext:", ciphertext)
    print("Decrypted :", decrypted)
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


BLOCK_SIZE = 16


# Encryption setup: the attacker does not receive the key
def encrypt_message(message):
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message, BLOCK_SIZE))

    return key, iv, ciphertext


# Oracle: reveals only whether PKCS#7 padding is valid
def create_oracle(key):
    queries = [0]

    def padding_oracle(data):
        queries[0] += 1

        if len(data) < 32 or len(data) % BLOCK_SIZE != 0:
            return False

        iv = data[:BLOCK_SIZE]
        ciphertext = data[BLOCK_SIZE:]

        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = cipher.decrypt(ciphertext)
            unpad(plaintext, BLOCK_SIZE)
            return True
        except ValueError:
            return False

    return padding_oracle, queries


# Attack function: does not receive or access the AES key
def padding_oracle_attack(iv, ciphertext, oracle):
    blocks = [
        ciphertext[i:i + BLOCK_SIZE]
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    previous = iv
    recovered = bytearray()

    for target in blocks:
        intermediate = bytearray(BLOCK_SIZE)
        plaintext_block = bytearray(BLOCK_SIZE)

        for pos in range(BLOCK_SIZE - 1, -1, -1):
            padding = BLOCK_SIZE - pos
            modified = bytearray(previous)

            for j in range(pos + 1, BLOCK_SIZE):
                modified[j] = (
                    intermediate[j] ^ padding
                )

            found = False

            for guess in range(256):
                modified[pos] = guess

                test = bytes(modified) + target

                if not oracle(test):
                    continue

                # Reject accidental valid padding
                if pos > 0:
                    check = bytearray(modified)
                    check[pos - 1] ^= 1

                    if not oracle(bytes(check) + target):
                        continue

                intermediate[pos] = guess ^ padding
                plaintext_block[pos] = (
                    intermediate[pos] ^ previous[pos]
                )

                found = True
                break

            if not found:
                raise RuntimeError(
                    f"Could not recover byte at position {pos}"
                )

        recovered.extend(plaintext_block)
        previous = target

    return bytes(recovered)


def main():
    message = (
        b"Padding oracle attacks recover plaintext "
        b"without knowing the AES key."
    )

    key, iv, ciphertext = encrypt_message(message)

    # The oracle internally holds the key.
    oracle, query_count = create_oracle(key)

    print("Ciphertext (hex):", ciphertext.hex())
    print("IV (hex):", iv.hex())

    # The attack receives only the IV, ciphertext and oracle.
    recovered = padding_oracle_attack(iv, ciphertext, oracle)

    # Remove PKCS#7 padding from the recovered plaintext.
    recovered = unpad(recovered, BLOCK_SIZE)

    print("\nRecovered plaintext:")
    print(recovered.decode("utf-8"))

    print("\nTotal oracle queries:", query_count[0])
    print("Recovery successful:", recovered == message)


if __name__ == "__main__":
    main()
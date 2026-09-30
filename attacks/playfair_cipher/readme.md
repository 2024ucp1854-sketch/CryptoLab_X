# Playfair Cipher

## Overview

This module implements the **Playfair Cipher**, a classical symmetric encryption technique that encrypts plaintext in pairs of letters (digraphs).

The implementation covers:

* Playfair key matrix generation
* Plaintext preprocessing
* Digraph formation
* Encryption
* Decryption
* Digraph frequency analysis
* Encryption/decryption verification

## Objectives

* Generate a 5 × 5 Playfair key matrix.
* Implement Playfair encryption.
* Implement Playfair decryption.
* Handle repeated letters and odd-length plaintext.
* Perform digraph frequency analysis.
* Verify the encryption and decryption process.

## Directory Structure

```text
playfair_cipher/
├── src/
│   └── main.cpp
├── input.txt
├── output.txt
├── README.md
└── notebook.txt
```

## Playfair Key Matrix

The Playfair cipher uses a 5 × 5 matrix.

The letters `I` and `J` are treated as one character.

For example, using the keyword:

```text
MONARCHY
```

the matrix becomes:

```text
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
```

## Plaintext Preparation

Before encryption:

1. Convert the plaintext to uppercase.
2. Remove spaces and special characters.
3. Replace `J` with `I`.
4. Divide the plaintext into pairs.
5. Insert `X` between repeated letters in a pair.
6. Add `X` if the final plaintext has an odd number of characters.

Example:

```text
BALLOON
```

is divided according to Playfair digraph rules.

## Encryption Rules

For every pair of letters:

### Same Row

Replace each letter with the letter immediately to its right.

### Same Column

Replace each letter with the letter immediately below it.

### Rectangle

If the letters form a rectangle, replace each letter with the character in the same row and the other character's column.

The matrix wraps around when the end of a row or column is reached.

## Decryption

Decryption uses the reverse operations:

* Same row → move left
* Same column → move up
* Rectangle → use the opposite corners

## Frequency Analysis

The program also performs digraph frequency analysis on the generated ciphertext.

It displays:

```text
Digraph    Frequency
--------------------
AB         3
XY         2
...
```

## Verification

The implementation verifies the result using:

```text
Plaintext
    ↓
Encryption
    ↓
Ciphertext
    ↓
Decryption
    ↓
Recovered Plaintext
```

The recovered plaintext is compared with the prepared plaintext.

```text
Verification: SUCCESS
```

## Compilation

From the `playfair_cipher` directory:

```bash
g++ src/main.cpp -o playfair
```

## Execution

```bash
./playfair
```

## Sample Input

```text
Keyword: MONARCHY
Plaintext: INSTRUMENTS
```

## Expected Operations

The program should display:

```text
Key Matrix

M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z

Prepared Plaintext:
INSTRUMENTS

Digraphs:
IN ST RU ME NT

Ciphertext:
...

Decrypted Text:
...

Verification:
SUCCESS
```

## Functions Implemented

```text
generate_key_matrix()
display_matrix()
clean_key()
find_position()

prepare_plaintext()
create_digraphs()
insert_filler()

playfair_encrypt()
encrypt_pair()

playfair_decrypt()
decrypt_pair()

digraph_frequency()
verify()
```

## Result

The Playfair Cipher is successfully implemented with key matrix generation, plaintext preparation, encryption, decryption, digraph frequency analysis, and verification.

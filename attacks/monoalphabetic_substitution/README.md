# Monoalphabetic Substitution Cipher and Cryptanalysis

## Aim

To implement a Monoalphabetic Substitution Cipher and perform its cryptanalysis using letter-frequency analysis, word-frequency analysis, repeated words, and word-pattern analysis.

## Objectives

* Implement monoalphabetic substitution encryption.
* Generate ciphertext from a plaintext message.
* Perform frequency analysis on the ciphertext.
* Analyze one-, two-, and three-letter words.
* Identify repeated words.
* Analyze repeated-letter patterns.
* Iteratively recover the plaintext using candidate substitutions.
* Recover the corresponding substitution key.
* Verify the recovered key by re-encrypting the plaintext.

## Problem Statement

A monoalphabetic substitution cipher replaces every plaintext alphabet character with a unique ciphertext character using a fixed substitution alphabet.

For this experiment, plaintext of at least one page is selected from *Introduction to Modern Cryptography* by Katz and Lindell according to the assigned group page. For Group 13, the assigned page is:

**Page = 13 + 30 = Page 43**

The plaintext is encrypted using a fixed substitution key. The resulting ciphertext is then analyzed to recover the original plaintext without directly knowing the key.

## Directory Structure

```text
monoalphabetic_substitution/
│
├── src/
│   ├── main.cpp
│   ├── substitution_cipher.cpp
│   ├── frequency_analysis.cpp
│   └── pattern_analysis.cpp
│
├── data/
│   ├── plaintext.txt
│   └── ciphertext.txt
│
└── README.md
```

## Modules

### 1. `substitution_cipher.cpp`

This module performs encryption using the monoalphabetic substitution key.

The plaintext alphabet is mapped to a shuffled ciphertext alphabet.

Example:

```text
Plain :  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher:  QWERTYUIOPASDFGHJKLZXCVBNM
```

Thus:

```text
A → Q
B → W
C → E
D → R
E → T
...
```

### 2. `frequency_analysis.cpp`

This module performs letter-frequency analysis.

It:

* Counts every ciphertext letter.
* Calculates the percentage frequency.
* Sorts letters in descending order of frequency.
* Displays the most frequent ciphertext letters.

Frequency analysis is useful because English letters have different occurrence frequencies.

### 3. `pattern_analysis.cpp`

This module performs:

* One-letter word analysis.
* Two-letter word analysis.
* Three-letter word analysis.
* Repeated-word analysis.
* Repeated-letter pattern analysis.

Examples of word patterns:

```text
MEET → ABBC
NOON → ABBA
THAT → ABCA
```

The pattern remains unchanged after monoalphabetic substitution.

### 4. `main.cpp`

The main program:

* Reads plaintext.
* Encrypts the plaintext.
* Saves the ciphertext.
* Calls frequency analysis.
* Calls word-frequency analysis.
* Calls pattern analysis.
* Performs substitution recovery.
* Displays partial plaintext.
* Verifies the recovered key.

## Required Functions

The implementation contains the following functions:

```text
frequency_analysis()
word_frequency_analysis()
pattern_analysis()
apply_substitution()
display_partial_plaintext()
verify_solution()
```

## Cryptanalysis Approach

The cryptanalysis is performed iteratively.

### Step 1: Frequency Analysis

Count the occurrences of each ciphertext letter and calculate its percentage.

Frequently occurring ciphertext letters are compared with frequently occurring English letters such as:

```text
E, T, A, O, I, N, S, H, R
```

A frequency match is treated only as a hypothesis.

### Step 2: Word Analysis

Analyze words based on their lengths.

Particular attention is given to:

```text
One-letter words
Two-letter words
Three-letter words
Repeated words
```

One-letter English words are usually `A` and `I`.

### Step 3: Pattern Analysis

Determine the repeated-letter structure of ciphertext words.

For example:

```text
XYYZ → ABBC
XQQX → ABBA
QXRQ → ABCA
```

These patterns are compared with possible English words.

### Step 4: Candidate Substitution

A possible mapping is proposed based on frequency, word structure, and pattern analysis.

For example:

```text
Q → E
```

The mapping is applied throughout the ciphertext.

### Step 5: Partial Plaintext

The resulting partial plaintext is displayed.

Known substitutions are shown while unknown characters remain unidentified.

Example:

```text
THE _E_T _E...
```

### Step 6: Accept or Reject

If the substitution produces meaningful English words and improves the plaintext, it is accepted.

If it produces meaningless or inconsistent text, it is rejected.

The process is repeated until the plaintext is recovered.

### Step 7: Key Recovery

After all substitutions have been identified, the complete substitution key is constructed.

The key must be one-to-one: two ciphertext letters cannot map to the same plaintext letter.

### Step 8: Verification

The recovered plaintext is encrypted again using the recovered key.

The newly generated ciphertext is compared with the original ciphertext.

If both are identical, the recovered key is considered valid.

## Compilation

Navigate to the assignment directory:

```bash
cd attacks/monoalphabetic_substitution
```

Compile:

```bash
g++ src/main.cpp src/substitution_cipher.cpp src/frequency_analysis.cpp src/pattern_analysis.cpp -o monoalphabetic
```

## Execution

Run:

```bash
./monoalphabetic
```

## Input

The plaintext is stored in:

```text
data/plaintext.txt
```

For this experiment, the plaintext is taken from the assigned page of Katz and Lindell's *Introduction to Modern Cryptography*.

## Output

The program generates:

```text
data/ciphertext.txt
```

and displays:

* Ciphertext generation status.
* Letter frequencies.
* Frequency percentages.
* Most frequent letters.
* One-letter words.
* Two-letter words.
* Three-letter words.
* Repeated words.
* Word patterns.
* Partial plaintext during cryptanalysis.
* Recovered substitution key.
* Verification result.

## Cryptanalysis Observation

During cryptanalysis, each important hypothesis is recorded using the following format:

| Step | Observation                              | Possible Substitution    | Substitution Tested | Result                      | Decision      |
| ---- | ---------------------------------------- | ------------------------ | ------------------- | --------------------------- | ------------- |
| 1    | Most frequent ciphertext letter observed | Candidate → E            | Tested candidate    | Partial plaintext examined  | Accept/Reject |
| 2    | One-letter word observed                 | Candidate → A/I          | Tested candidate    | Word structure examined     | Accept/Reject |
| 3    | Common two-letter word observed          | Candidate mapping        | Tested mapping      | Partial plaintext improved  | Accept/Reject |
| 4    | Repeated three-letter word observed      | Candidate → THE/AND/etc. | Tested mapping      | Meaningful words obtained   | Accept/Reject |
| 5    | Repeated-letter pattern observed         | Pattern-based candidate  | Tested mapping      | Pattern matched             | Accept/Reject |
| 6    | Several words became meaningful          | Multiple mappings        | Tested mappings     | Plaintext improved          | Accept        |
| 7    | Remaining mappings identified            | Remaining candidates     | Tested mappings     | Complete plaintext obtained | Accept        |

The actual observations and substitutions should be filled using the results obtained from the experiment.

## Important Properties

### Fixed Substitution

The same plaintext letter always maps to the same ciphertext letter.

### One-to-One Mapping

Each plaintext letter has a unique ciphertext equivalent.

### Preserved Word Length

Spaces and punctuation are not substituted, so word boundaries and word lengths remain visible.

### Preserved Letter Patterns

Repeated letters within a word remain repeated after encryption.

## Limitations

Monoalphabetic substitution is vulnerable to cryptanalysis because:

* Letter frequencies are preserved.
* Word lengths remain unchanged.
* Repeated words remain repeated.
* Repeated-letter patterns remain unchanged.
* Common English words provide useful clues.

Therefore, a sufficiently long ciphertext can often be attacked using frequency and pattern analysis.

## Result

The Monoalphabetic Substitution Cipher was successfully implemented. Ciphertext was generated from the plaintext, and cryptanalysis was performed using frequency analysis, word analysis, and pattern analysis. Candidate substitutions were tested iteratively to recover the plaintext and substitution key. The recovered key was verified by re-encrypting the plaintext and comparing the resulting ciphertext with the original ciphertext.

import os
from collections import Counter

def analyze_file(filename):

    filepath = os.path.join("datasets", filename)

    if not os.path.exists(filepath):
        print("File not found!")
        return

    with open(filepath, "r") as file:
        text = file.read()

    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    unique_characters = len(set(text))

    letters = [ch.lower() for ch in text if ch.isalpha()]
    frequency = Counter(letters)

    print("\n========== File Analysis ==========")
    print("Characters        :", characters)
    print("Words             :", words)
    print("Lines             :", lines)
    print("Unique Characters :", unique_characters)

    print("\nLetter Frequency")

    for letter in "abcdefghijklmnopqrstuvwxyz":
        print(f"{letter} : {frequency.get(letter, 0)}")
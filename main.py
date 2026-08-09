from analysis.file_analysis import analyze_file
from utils.logger import log_action

while True:
    print("\n========== CryptoLabX ==========")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        log_action("Encrypt")
        print("\nEncrypt Module")
        print("Coming Soon...")

    elif choice == "2":
        log_action("Decrypt")
        print("\nDecrypt Module")
        print("Coming Soon...")

    elif choice == "3":
        log_action("Attack")
        print("\nAttack Module")
        print("Coming Soon...")

    elif choice == "4":
        log_action("Analyze")
        filename = input("Enter file name (e.g., text1.txt): ")
        analyze_file(filename)

    elif choice == "5":
        log_action("Exit")
        print("\nThank you for using CryptoLabX.")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
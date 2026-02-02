import hashlib

# Global variables
stored_text = None
stored_hash = None


def enter_text():
    global stored_text
    stored_text = input("\nEnter text to hash: ")
    print("Text stored successfully\n")


def generate_hash_menu():
    global stored_text, stored_hash

    if stored_text is None:
        print("\nEnter text first.\n")
        return

    sha = hashlib.sha256()
    sha.update(stored_text.encode())
    stored_hash = sha.hexdigest()

    while True:
        print("\n===== SHA256 HASH OUTPUT =====")
        print(stored_hash)
        print("\n4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "4":
            break
        else:
            print("Invalid choice")


def verify_hash_menu():
    global stored_hash

    if stored_hash is None:
        print("\nGenerate hash first.\n")
        return

    verify_text = input("\nEnter text to verify: ")

    sha = hashlib.sha256()
    sha.update(verify_text.encode())
    verify_hash = sha.hexdigest()

    while True:
        print("\n===== HASH VERIFICATION RESULT =====")

        if verify_hash == stored_hash:
            print("Match: Text is valid")
        else:
            print("Not Match: Text is different")

        print("\n4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "4":
            break
        else:
            print("Invalid choice")


def main_menu():
    while True:
        print("\n====== SHA Hash Tool ======")
        print("1. Enter Text")
        print("2. Generate SHA256 Hash")
        print("3. Verify Hash")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_text()
        elif choice == "2":
            generate_hash_menu()
        elif choice == "3":
            verify_hash_menu()
        elif choice == "4":
            print("\nExiting Program")
            break
        else:
            print("Invalid choice")


main_menu()

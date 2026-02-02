from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Global variables
public_key = None
private_key = None
message = None
encrypted_message = None


def generate_keys():
    global public_key, private_key

    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    print("\nRSA Keys Generated Successfully\n")


def enter_message():
    global message
    user_input = input("\nEnter your message: ")
    message = user_input.encode()
    print("Message stored successfully\n")


def encrypt_menu():
    global encrypted_message, message, public_key

    if public_key is None:
        print("\nGenerate keys first.\n")
        return

    if message is None:
        print("\nEnter message first.\n")
        return

    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message)

    encrypted_display = base64.b64encode(encrypted_message).decode()

    while True:
        print("\n===== RSA ENCRYPTED MESSAGE =====")
        print(encrypted_display)
        print("\n5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "5":
            break
        else:
            print("Invalid choice")


def decrypt_menu():
    global encrypted_message, private_key

    if private_key is None:
        print("\nGenerate keys first.\n")
        return

    if encrypted_message is None:
        print("\nEncrypt message first.\n")
        return

    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(encrypted_message)

    while True:
        print("\n===== RSA DECRYPTED MESSAGE =====")
        print(decrypted.decode())
        print("\n5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "5":
            break
        else:
            print("Invalid choice")


def main_menu():
    while True:
        print("\n====== RSA Encryption Tool ======")
        print("1. Generate Keys")
        print("2. Enter Message")
        print("3. Encrypt Message")
        print("4. Decrypt Message")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_keys()
        elif choice == "2":
            enter_message()
        elif choice == "3":
            encrypt_menu()
        elif choice == "4":
            decrypt_menu()
        elif choice == "5":
            print("\nExiting Program")
            break
        else:
            print("Invalid choice")


main_menu()

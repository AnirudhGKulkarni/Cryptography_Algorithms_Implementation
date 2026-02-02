from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# Global variables
key = get_random_bytes(16)
ciphertext = None
message = None
iv = None


def enter_message():
    global message
    user_input = input("\nEnter your message: ")
    message = user_input.encode()
    print("Message stored successfully.\n")


def encrypt_menu():
    global ciphertext, message, iv

    if message is None:
        print("\nNo message found. Please enter message first.\n")
        return

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(message, AES.block_size))

    encrypted_display = base64.b64encode(ciphertext).decode()

    while True:
        print("\n===== ENCRYPTED MESSAGE =====")
        print(encrypted_display)
        print("\n4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "4":
            break
        else:
            print("Invalid choice")


def decrypt_menu():
    global ciphertext, key, iv

    if ciphertext is None:
        print("\nNo encrypted message found. Please encrypt first.\n")
        return

    decipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

    while True:
        print("\n===== DECRYPTED MESSAGE =====")
        print(plaintext.decode())
        print("\n4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "4":
            break
        else:
            print("Invalid choice")


def main_menu():
    while True:
        print("\n====== AES Encryption Tool ======")
        print("1. Enter Message")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_message()
        elif choice == "2":
            encrypt_menu()
        elif choice == "3":
            decrypt_menu()
        elif choice == "4":
            print("\nExiting Program")
            break
        else:
            print("Invalid choice")


main_menu()

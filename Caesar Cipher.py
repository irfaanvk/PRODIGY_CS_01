# Function to encrypt the message using Caesar Cipher
def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabet characters unchanged
        else:
            encrypted_message += char

    return encrypted_message


# Function to decrypt the message using Caesar Cipher
def decrypt(message, shift):
    return encrypt(message, -shift)


# Main program
def main():
    # Asking user for choice: encrypt or decrypt
    choice = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if choice == 'encrypt':
        message = input("Enter your message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice == 'decrypt':
        message = input("Enter your message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

    else:
        print("Invalid choice, please enter 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()

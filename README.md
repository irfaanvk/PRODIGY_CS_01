PRODIGY_CS_01
Caesar Cipher - Simple Text Encryption and Decryption

Welcome to the Caesar Cipher project! This is a Python program that allows users to easily encrypt and decrypt messages using one of the simplest and oldest encryption techniques—the Caesar Cipher. Whether you're learning about encryption or just exploring fun ways to manipulate text, this project provides a hands-on experience with classic cryptography.

What is the Caesar Cipher? The Caesar Cipher is a substitution cipher, one of the oldest known forms of encryption, named after Julius Caesar, who reportedly used it to protect his private messages. In this cipher, each letter in the plaintext (original message) is shifted by a certain number of positions in the alphabet. For example, with a shift of 3, A becomes D, B becomes E, and so on. When decrypting, the process is reversed, shifting letters back to their original form.

How Does This Program Work? This Python implementation of the Caesar Cipher allows users to: Encrypt a message by shifting each letter in the message by a user-specified number of positions in the alphabet. Decrypt a previously encrypted message by reversing the shift and recovering the original message. The program supports both uppercase and lowercase letters, while leaving special characters (such as spaces, punctuation, or numbers) unchanged.

Why Use This Program? This program is perfect for anyone interested in understanding how basic encryption works. It provides an interactive way to learn how simple ciphers function, and it can even be a starting point for experimenting with more complex cryptographic techniques.

How to Use the Program? Getting started with the Caesar Cipher program is easy. Just follow these steps:

Clone the repository to your local machine: git clone https://github.com/irfaanvk/PRODIGY_CS_01

Navigate to the project directory: cd caesar-cipher

Run the program: python task.py

Once the program is running, you'll be prompted to choose whether you want to encrypt or decrypt a message. After selecting your option, you'll input your message and a shift value (a positive integer). The program will then output the encrypted or decrypted message, depending on your choice.

Example in Action Here’s a quick example of what it looks like to encrypt a message:

Input: Do you want to encrypt or decrypt? encrypt Enter your message: hello Enter shift value: 3 Output: Encrypted Message: khoor

To decrypt that message, you would input: Input: Do you want to encrypt or decrypt? decrypt Enter your message: khoor Enter shift value: 3 Output: Decrypted Message: hello

Conclusion The Caesar Cipher may be simple, but it’s a great introduction to the world of cryptography. With this program, you can explore the basics of encryption, see how text can be transformed, and gain a deeper appreciation for the importance of securing information. Give it a try and see how easily you can transform a simple message!


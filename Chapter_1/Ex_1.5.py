# Exercise 1.5
# IDENTIFYING THE DICTIONARY

import string
import random

text = input("Enter the text: ")
key = int(input("Enter the key value: "))

def mapping(key):

    alphabet = string.ascii_uppercase

    alpha_list = list(alphabet)
    random.seed(key)
    random.shuffle(alpha_list)
    jumbled = "".join(alpha_list)

    encrypt_dict = dict(zip(alphabet, jumbled))
    decrypt_dict = dict(zip(jumbled, alphabet))

    return encrypt_dict, decrypt_dict

#print(f"{mapping(key)}")

def encrypt(message):
    upp = message.upper()
    encrypt_d, _ = mapping(key)
    cipher_text = ""
    for char in upp:
        if char.isalpha():
            k = encrypt_d[char]
            cipher_text += k
    return cipher_text

def decrypt(ci_text):
    _ , decrypt_d = mapping(key)
    decoded_text = ""
    for char in ci_text:
        if char.isalpha():
            k = decrypt_d[char]
            decoded_text += k
    return decoded_text

print(f"The encrypted text is:\n{encrypt(text)}")
print(f"The decoded text is:\n{decrypt(encrypt(text))}")


# for files

file_name = input("Enter the file name: ")
key = int(input("Enter the key value: "))

def mapping(key):

    alphabet = string.ascii_uppercase

    alpha_list = list(alphabet)
    random.seed(key)
    random.shuffle(alpha_list)
    jumbled = "".join(alpha_list)

    encrypt_dict = dict(zip(alphabet, jumbled))
    decrypt_dict = dict(zip(jumbled, alphabet))

    return encrypt_dict, decrypt_dict

try:
    with open(file_name, "r") as file:
        content = file.read()
        upp = content.upper()

        def encrypt(message):
            encrypt_d, _ = mapping(key)
            cipher_text = ""
            for char in message:
                if char.isalpha():
                    k = encrypt_d[char]
                    cipher_text += k
            return cipher_text
        
        def decrypt(ci_text):
            _ , decrypt_d = mapping(key)
            decoded_text = ""
            for char in ci_text:
                if char.isalpha():
                    k = decrypt_d[char]
                    decoded_text += k
            return decoded_text
        
        print(f"\nThe encrypted text is:\n{encrypt(upp)}")
        print(f"\nThe decoded text is:\n{decrypt(encrypt(upp))}\n")

except FileNotFoundError:
    print("File not found!")

# Exercise 1.3
# A STRONG SUBSTITUTION CIPHER
# By shuffling the alphabet

import string
import random

file_name = input("Enter the file name: ")

alphabet = string.ascii_uppercase

list_alpha = list(alphabet)
random.shuffle(list_alpha)
jumbled_alpha = "".join(list_alpha)

encode_dict = dict(zip(alphabet,jumbled_alpha))
decode_dict = dict(zip(jumbled_alpha,alphabet))

try:
    with open(file_name, "r") as file:

        content = file.read()
        upp = content.upper()

        def encode(message):
            cipher_text = ""
            for char in message:
                if char.isalpha():
                    k = encode_dict[char]
                    cipher_text += k
            return cipher_text
        
        print(f"The cipher text is:\n{encode(upp)}")

        def decode(ci_text):
            decoded_text = ""
            for char in ci_text:
                k = decode_dict[char]
                decoded_text += k
            return decoded_text
        
        print(f"\nThe decoded text is:\n{decode(encode(upp))}\n")


except FileNotFoundError:
    print("File not found!")

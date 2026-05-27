# Exercise 1.1

import string

#for one shift
def encode(plain_text):
    cipher_f = ""
    alphabet_size = len(string.ascii_uppercase)
    for char in plain_text:
        ascii_value = ord(char)
        #shifting
        k = string.ascii_uppercase[(ascii_value - 13 + 1) % alphabet_size]
        cipher_f += k
    return cipher_f
    

pt = input("Enter the plain text (in Capital letters): ")
print(f"The cipher text for given plaint text: {encode(pt)}")

def decode(ci_text):
    decode_f = ""
    alphabet_size = len(string.ascii_uppercase)
    for char in ci_text:
        ascii_value = ord(char)
        k = string.ascii_uppercase[(ascii_value - 13 - 1) % alphabet_size]
        decode_f += k
    return decode_f
    
print(f"The decoded text is: {decode(encode(pt))}")


#for user input shift (can be positive, negative or 0)
def encode(plain_text,n):
    cipher_f = ""
    alphabet_size = len(string.ascii_uppercase)
    for char in plain_text:
        ascii_value = ord(char)
        k = string.ascii_uppercase[(ascii_value - 13 + n) % alphabet_size]
        cipher_f += k
    return cipher_f
    

pt = input("Enter the plain text (in Capital letter): ")
s = int(input("Enter the size of shift: "))
print(f"The cipher text for given plaint text: {encode(pt,s)}")

def decode(ci_text):
    decode_f = ""
    alphabet_size = len(string.ascii_uppercase)
    for char in ci_text:
        ascii_value = ord(char)
        k = string.ascii_uppercase[(ascii_value - 13 - s) % alphabet_size]
        decode_f += k
    return decode_f
    
print(f"The decoded text is: {decode(encode(pt,s))}")

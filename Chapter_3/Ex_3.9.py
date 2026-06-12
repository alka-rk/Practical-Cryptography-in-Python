# Exercise 3.9
# THE MASK OF XOR-O?

import os

message = input("Enter plaintext of 16 byte (i.e length): ")

iv = os.urandom(16)

ciphertext = bytearray()
for i in range(16):
    ciphertext.append(message.encode()[i] ^ iv[i])

print(f"Ciphertext: {ciphertext}")

rec_plaintext = bytearray()
for i in range(16):
    rec_plaintext.append(ciphertext[i] ^ iv[i])

print(f"Recovered plaintext: {rec_plaintext.decode()}")
# Exercise 3.13
# WRITE A SIMPLE COUNTER MODE

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

plaintext = input("Enter plaintext: ")

iv = os.urandom(8)

num = 0
i = 0
ciphertexts = []
keys = []

for i in range(0, len(plaintext), 16):

    block = plaintext[i:i+16]
    key = os.urandom(16)
    keys.append(key)
    nonce = str(num).zfill(8)
    counter = iv + nonce.encode()
    num += 1
    
    cipher = Cipher(algorithms.AES(key), modes.ECB(),backend=default_backend)
    aesEncrypter = cipher.encryptor()

    encrypt = aesEncrypter.update(counter)

    ct = bytes(x^y for x,y in zip(encrypt, block.encode()))
    ciphertexts.append(ct)

    i += 1

num = 0
i = 0
recovered_texts = b''

for ct in ciphertexts:

    nonce = str(num).zfill(8)
    counter = iv + nonce.encode()
    num += 1

    cipher = Cipher(algorithms.AES(keys[i]), modes.ECB(),backend=default_backend)
    aesEncrypter = cipher.encryptor()

    encrypt = aesEncrypter.update(counter)

    pt = bytes(x^y for x,y in zip(encrypt, ct))
    recovered_texts += pt

    i += 1

print(f"Recovered text: {recovered_texts.decode()}")
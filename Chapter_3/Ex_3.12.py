# Exercise 3.12
# HAND-CRAFTED CBC

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

plaintext = input("Enter the plaintext: ")

key = os.urandom(32)
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend)

aesEncrypter = cipher.encryptor()
aesDecrypter = cipher.decryptor()

padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

padded_plaintext = padder.update(plaintext.encode())
padded_plaintext += padder.finalize()

ciphertexts = []
previous = iv

for i in range(0, len(padded_plaintext), 16):

    block = padded_plaintext[i:i+16]
    xor = bytes(x^y for x,y in zip(previous,block))
    ct = aesEncrypter.update(xor)
    ciphertexts.append(ct)
    previous = ct

aesEncrypter.finalize()

decoded_text = b''

ct = ciphertexts[0]
previous = iv

for ct in ciphertexts:

    decryp = aesDecrypter.update(ct)
    rev_xor = bytes(x^y for x,y in zip(decryp,previous))
    previous = ct
    decoded_text += rev_xor

aesDecrypter.finalize()

unpadded_message = unpadder.update(decoded_text)
unpadded_message += unpadder.finalize()

print(f"Recovered text: {unpadded_message.decode()}")
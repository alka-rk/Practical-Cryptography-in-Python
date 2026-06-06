# Exercise 3.1
# A SECRET MESSAGE

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
aesCipher = Cipher(algorithms.AES(key),
                    modes.ECB(),
                    backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

plaintext = 'a secret message'

ciphertext = aesEncryptor.update(plaintext.encode())
print(f"Ciphertext: {ciphertext}")

decoded = aesDecryptor.update(ciphertext)
print(f"Decoded text: {decoded.decode()}")

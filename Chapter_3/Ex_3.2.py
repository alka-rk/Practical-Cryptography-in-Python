# Exercise 3.2
# UPDATED TECHNOLOGY

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encryption(message, key):
    key = key.encode()

    if len(key) != 16:
        raise ValueError("Key must be exactly 16 characters.")

    padder = padding.PKCS7(128).padder()
    plain_text = padder.update(message.encode()) + padder.finalize()
    aesCipher = Cipher(algorithms.AES(key),modes.ECB(),backend=default_backend) 
    aesEncryptor = aesCipher.encryptor()

    cipher_text = aesEncryptor.update(plain_text) + aesEncryptor.finalize()

    return cipher_text

def decryption(ci_text, key):

    unpadder = padding.PKCS7(128).unpadder()
    
    aesCipher = Cipher(algorithms.AES(key.encode()),modes.ECB(),backend=default_backend) 
    aesDecryptor = aesCipher.decryptor()
    padded_plaintext = aesDecryptor.update(ci_text) + aesDecryptor.finalize()
    plain_text = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plain_text.decode()



message = input("Enter plain text: ")
key_ = input("Enter 16 byte key: ") # The length of key should be 16

print(f"Ciphertext: {encryption(message, key_).hex()}")
print(f"Decoded text: {decryption(encryption(message, key_),key_)}")
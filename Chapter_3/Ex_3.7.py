# Exercise 3.7
# SENDING BOB A FAKE MESSAGE

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend)

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

# Message from Alice to Bob

def message1():

    Message = b""" FROM: FIELD AGENT ALICE
    TO: FIELD AGENT BOB
    RE: Meeting
    DATE: 2001-1-1

    Meet me today at the docks at 2300."""
    Message +=b'E' * (-len(Message) % 16)

    encrypted = aesEncryptor.update(Message)
    return encrypted

def message2():

    Message = b""" FROM: FIELD AGENT ALICE
    TO: FIELD AGENT BOB
    RE: Meeting
    DATE: 2001-1-2

    Meet me today at the Che coffee at 22:00."""
    Message +=b'E' * (-len(Message) % 16)

    encrypted = aesEncryptor.update(Message)
    return encrypted

ciphertext1 = message1().hex()
ciphertext2 = message2().hex()

len_ci1 = len(ciphertext1)
len_ci2 = len(ciphertext2)

# Replacing the last block of the newer message with the last blocks of the previous message
for i in range(3):
    new_text = ciphertext2.replace(ciphertext2[len_ci2-32:len_ci2],ciphertext1[len_ci1-32:len_ci1])
    print(aesDecryptor.update(bytes.fromhex(new_text)).decode(),"\n")

    len_ci1 -= 32
    len_ci2 -= 32
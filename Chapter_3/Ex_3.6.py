# Exercise 3.6
# SENDING BOB A MESSAGE

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

# Message from Bob to Alice

def message3():

    Message = b""" FROM: FIELD AGENT BOB
    TO: FIELD AGENT ALICE
    RE: Meeting
    DATE: 2001-1-1

    Busy today. Reschedule to tomorrow."""
    Message +=b'E' * (-len(Message) % 16)

    encrypted = aesEncryptor.update(Message)
    return encrypted

def message4():

    Message = b""" FROM: FIELD AGENT BOB
    TO: FIELD AGENT ALICE
    RE: Meeting
    DATE: 2001-1-2

    Okay."""
    Message +=b'E' * (-len(Message) % 16)

    encrypted = aesEncryptor.update(Message)
    return encrypted

print(aesDecryptor.update(message1()).decode(),"\n")
print(aesDecryptor.update(message3()).decode(),"\n")
print(aesDecryptor.update(message2()).decode(),"\n")
print(aesDecryptor.update(message4()).decode(),"\n")
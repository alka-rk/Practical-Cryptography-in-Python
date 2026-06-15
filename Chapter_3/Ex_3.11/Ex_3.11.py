from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Image encryption using ECB

key = os.urandom(16)

aesCipher = Cipher(
    algorithms.AES(key),
    modes.ECB(),
    backend=default_backend()
)

aesEncryptor = aesCipher.encryptor()

with open("image.bmp", "rb") as reader:
    with open("encrypted_byECB.bmp", "wb+") as writer:

        image_data = reader.read()

        # BMP header (54 bytes)
        header = image_data[:54]

        # Pixel data
        body = image_data[54:]

        # Pad to a multiple of 16 bytes
        if len(body) % 16 != 0:
            body += b"\x00" * (16 - (len(body) % 16))

        encrypted_body = aesEncryptor.update(body)
        encrypted_body += aesEncryptor.finalize()

        writer.write(header + encrypted_body)

# Image encryption by CBC

key = os.urandom(32)
iv = os.urandom(16)

aesCipher = Cipher(
    algorithms.AES(key),
    modes.CBC(iv),
    backend=default_backend()
)

aesEncryptor = aesCipher.encryptor()

with open("image.bmp", "rb") as reader:
    with open("encrypted_byCBC.bmp", "wb+") as writer:

        image_data = reader.read()

        # BMP header (54 bytes)
        header = image_data[:54]

        # Pixel data
        body = image_data[54:]

        # Pad to a multiple of 16 bytes
        if len(body) % 16 != 0:
            body += b"\x00" * (16 - (len(body) % 16))

        encrypted_body = aesEncryptor.update(body)
        encrypted_body += aesEncryptor.finalize()

        writer.write(header + encrypted_body)
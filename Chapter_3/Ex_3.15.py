# Exercise 3.15
# RIDING THE KEYSTREAM

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)
iv = os.urandom(8)

cipher = Cipher(algorithms.AES(key), modes.ECB(),backend=default_backend())
aesEncrypter = cipher.encryptor()

def encrypt(plaintext):

    num = 0
    i = 0
    ciphertexts = []

    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        nonce = str(num).zfill(8)
        counter = iv + nonce.encode()
        num += 1
        
        encrypt = aesEncrypter.update(counter)

        ct = bytes(x^y for x,y in zip(encrypt, block.encode()))
        ciphertexts.append(ct.hex())

    return "".join(ciphertexts)

plaintext1 = """
<XML>
    <CreditCardPurchase>
        <Merchant>Acme Inc</Merchant>
        <Buyer>John Smith</Buyer>
        <Date>01/01/2001</Date>
        <Amount>$100.00</Amount>
        <CCNumber>555-555-555-555</CCNumber
    </CreditCardPurchase>
</XML>
"""
plaintext2 = """
<XML>
    <CreditCardPurchase>
        <Merchant>Acme Inc</Merchant>
        <Buyer>Sara John</Buyer>
        <Date>02/01/2001</Date>
        <Amount>$153.00</Amount>
        <CCNumber>555-897-575-950</CCNumber
    </CreditCardPurchase>
</XML>
"""
# Known ciphertexts for both plaintexts
ciphertext1 = encrypt(plaintext1)
ciphertext2 = encrypt(plaintext2)

# Finding the keystream
ct1_bytes = bytes.fromhex(ciphertext1)
keystream = bytes(x^y for x,y in zip(ct1_bytes,plaintext1.encode()))

# Recovering the unknown plaintext
ct2_bytes = bytes.fromhex(ciphertext2)
recovered_pt2 = bytes(x^y for x,y in zip(ct2_bytes,keystream))
print(f"Recovered plaintext:\n{recovered_pt2.decode()}")
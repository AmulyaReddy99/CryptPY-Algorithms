#!/usr/bin/env python3 -tt
"""
File: crypto.py
Name: AMULYA REDDY
"""
import utils
import random
from math import gcd as bltin_gcd


# Caesar Cipher

def encrypt_caesar(plaintext):
    for i in range(len(plaintext)):
        x=ord(text[i])+3
        if x<ord('z'):
            ciphertext+=chr(x)
        else:
            ciphertext+=chr(x-26)
    print(ciphertext)


def decrypt_caesar(ciphertext):
    for i in range(len(ciphertext)):
        x=ord(text[i])-3
        if x>ord('a'):
            plaintext+=chr(x)
        else:
            plaintext+=chr(x+26)
    print(plaintext)



    """
    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back
    """

    
def intel_codebreaker(ciphertext):
    with open file as f1,f2:
        word_file = f2.readfile()
        keyword = f1.read()
        plaintext = decrypt_vigenere(ciphertext, keyword)
        if plaintext in word_file:
            return plaintext


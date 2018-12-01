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


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    for i in range(len(plaintext)):
        x=(ord(plaintext[i])-2*ord('a')+ord(keyword[i]))%26+ord('a')
        ciphertext+=chr(x)
    print(ciphertext)   


def decrypt_vigenere(ciphertext, keyword):
    for i in range(len(ciphertext)):
        x=ord(ciphertext[i])-ord(keyword[i])
        if x>=0:
            plaintext+=chr(x+ord('a'))
        else:
            plaintext+=chr(26+x+ord('a'))
    print(plaintext) 


# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    for i in range(n):
        superincreasing_sequence.append(sum(superincreasing_sequence)+random.randint(2,10)) 
    q=sum(superincreasing_sequence)+random.randint(2,20)
    r=0
    while bltin_gcd(r, q) != 1:
        r=random.randint(2,q-1)
    #return(r,q,superincreasing_sequence)


def create_public_key(private_key):
    r,q,w = private_key
    b=[(r*w[i])%q for i in range(n)]
    return b


def encrypt_mh(message, public_key):
    a=[byte_to_bits(ord(message[i])) for i in range(len(message))]
    c=sum([a[i]*b[i] for i in range(n)])
    return c


def decrypt_mh(message, private_key):
    #must be modified furthur
    r,q,w = private_key
    s = utils.modinv(r, q)
    c1 = c*s%q
    c1 = [sum(a[i]*w[i]) for i in range(n)] #?
    while n<8:
        w_k=max(w)
        if w_k>c1: a_k=0
        else: a_k=1
        alpha=c1-w_k*a_k

    """
    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back
    """

def scylate_encrypt(plaintext, circumference):
    for i in range(len(plaintext)//circumference+1):
        for j in range(0,len(plaintext),circumference):
            ciphertext+=plaintext[i+j]
        

def scylate_decrypt(ciphertext, circumference):
    size=len(ciphertext)//circumference
    for i in range(len(ciphertext)//size-1):
        for j in range(0,len(ciphertext),size):
            plaintext+=ciphertext[i+j]


def railfence_encrypt(plaintext, circumference):
    #not full
    size=2*(circumference-1)
    for i in range(circumference):
        for j in range(0,len(plaintext),size):
            ciphertext+=plaintext[i+j]
        size=size//2


def railfence_decrypt(ciphertext, circumference):
    #not full
    size=2*(circumference-1)
    for i in range(circumference):
        for j in range(0,len(plaintext),size):
            ciphertext+=plaintext[i+j]
        size=size//2


def intel_codebreaker(ciphertext):
    with open file as f1,f2:
        word_file = f2.readfile()
        keyword = f1.read()
        plaintext = decrypt_vigenere(ciphertext, keyword)
        if plaintext in word_file:
            return plaintext


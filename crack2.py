#!/usr/bin/env python3

import time

in_f = open("check.txt","r")
in_d = in_f.read()

out_f = open("out.txt","r")
out_d = out_f.read()


keys_i = []
keys_c = ""

i=0

for char in in_d:
    in_c = ord(char)
    out_c = ord(out_d[i])
   
    for j in range(256):
        if (in_c + j ) % 255 == out_c:
            keys_i.append(j)
            keys_c+=chr(j)

    i+=1


	



def encrypt(text, key):
    keylen = len(key)
    keyPos = 0
    encrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr + ord(keyChr)) % 255)
        encrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen

    return encrypted

def decrypt(text, key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)
        decrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return decrypted

print(keys_c)
k = open("key.txt","w")
k.write(keys_c)
print
print(encrypt(in_d, keys_c[:92]))
print
print(decrypt(out_d,keys_c[:92]))


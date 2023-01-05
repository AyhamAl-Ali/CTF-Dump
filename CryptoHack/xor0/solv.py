#!/usr/bin/env python3

string = "label"
key = 13

#! Easy Solve!
# from pwn import *
# print("crypto{{{0}}}".format(xor('label', 13)))


#! Manual Solve

# Testing
# print(bin(13)[2:]) # Filter '0b'

def xor(string, key):
    res = ''
    for c in string:
        # for n in key:
        res += chr(ord(c) ^ key)
    return res

print("crypto{{{0}}}".format(xor(string, key)))
    
    
# Flag: crypto{aloha}
#!/usr/bin/env python3

from pwn import *

with open("space_encoded.txt", "rb") as bin_file:
    for _ in range(88):
        data = bytearray(bin_file.readline())
        data = data.replace(b'\x09', b'1')
        data = data.replace(b'\x20', b'0')
        data = data.replace(b'\x0d', b'')
        data = data.replace(b'\x0a', b'')
        data = data.decode("ascii")
        if unbits(data) == b'\x80': # ignored single 1's
            continue
        print(data,end = ' ')
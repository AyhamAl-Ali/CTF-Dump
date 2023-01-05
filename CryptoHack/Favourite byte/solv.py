#!/usr/bin/env python3

xor_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
xor_string_arr = [x for x in bytes.fromhex(xor_string) ]

for x in range(127):
    f = "".join(([chr(o ^ x) for o in xor_string_arr]))
    if str.__contains__(f, "crypto"):
        print(f)
        print(x)
        print(hex(x))
        break

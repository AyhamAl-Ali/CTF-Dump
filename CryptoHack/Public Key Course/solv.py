#!/usr/bin/env python3

#! Remember the flag format and how it might help you in this challenge! (crypto{)

xor_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
xor_string_arr = [x for x in bytes.fromhex(xor_string)]
# print(len(xor_string_arr)) # 42

# print([*"crypto{"])
# print(xor_string_arr[:7])

# print(zip(xor_string_arr[:7], [*"crypto{"]))
# print("".join([chr(x ^ ord(f)) for (x, f) in zip(xor_string_arr[:7], [*"crypto{"])])) # myXORke (assume it's myXORkey)

#! manual solution
# print("".join([chr(x ^ ord(f)) for (x, f) in zip(xor_string_arr, [*"myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymy"])])) 

#! Better Solution
key = ("myXORkey" * 6)[:-6] # we only need 42 char length key
print(key)
print("".join([chr(x ^ ord(f)) for (x, f) in zip(xor_string_arr, [*key])])) 

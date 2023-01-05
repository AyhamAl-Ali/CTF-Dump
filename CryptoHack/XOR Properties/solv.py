#!/usr/bin/env python3

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 

# Solution Ref: https://github.com/s-nikravesh/crypto-hack/blob/master/General/XOR%20Properties.py

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# looping each hex code will return its ordinary number
# putting them all in [] will return them as an array
k1_ord = [o for o in bytes.fromhex(k1)]
k2_k3_ord = [o for o in bytes.fromhex(k2_k3)]
flag_k1_k3_k2_ord = [o for o in bytes.fromhex(flag_k1_k3_k2)]

#! Debugging
# print(k1_ord)
# print(k2_k3_ord)
# print(flag_k1_k3_k2_ord)

# XORing flag_k1_k3_k2_ord with k2_k3_ord will kinda like extract k2_k3_ord from flag_k1_k3_k2_ord leaving you with flag_k1_ord
flag_k1_ord = [
    o_f132 ^ o23 for (o_f132, o23) in zip(flag_k1_k3_k2_ord, k2_k3_ord)
]

# XORing flag_k1_ord with k1_ord will kinda like extract k1_ord from flag_k1_ord leaving you with flag_ord
flag_ord = [o_f1 ^ o1 for (o_f1, o1) in zip(flag_k1_ord, k1_ord)]

# Finally return the char value of each ord
flag = "".join(chr(o) for o in flag_ord)

print("Flag:")
print(flag)

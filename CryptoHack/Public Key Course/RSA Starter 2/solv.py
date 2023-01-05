#!/usr/bin/env python3

#! "Encrypt" the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23. What number do you get as the ciphertext? 
p = 17
q = 23
N = p * q
e = 65537
m = 12

print (pow(m, e, N))
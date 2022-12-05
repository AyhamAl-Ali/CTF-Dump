from random import randint

# Copyrights reserved to author at m0lecon CTF
# Forked version of the scramble challenge
# https://github.com/AyhamAl-Ali/CTF-Dump/tree/main/CTFs/m0lecon/scramble

flag = "GUoPr{}I_Y}u_0}r0}fW01}h_t}F__L}I_Ypt'}ute304!"

assert(len(flag) <= 50)
shift = randint(1, len(set(flag)) - 1)

def encrypt(data):
    charsf = {}
    for c in data:
        if c not in charsf.keys():
            charsf[c] = 1
        else:
            charsf[c] += 1

    chars = list(charsf.keys())
    chars.sort(reverse=True, key=lambda e: charsf[e])

    charsn = list(chars)
    for _ in range(shift):
        i = charsn.pop(0)
        charsn.append(i)

    enc = "".join(list(map(lambda c: charsn[chars.index(c)], data)))
    return enc

if __name__ == "__main__":
    print("Encrypt the un-encrypted")
    print("1) Encrypt")
    print("2) Print Flag")
    print("3) Explode")

    opt = input("> ")
    while opt != "3":
        if opt == "1":
            data = input("Yooooour text?\n")
            print(encrypt(data))
        elif opt == "2":
            print(encrypt(flag))
        opt = input("> ")

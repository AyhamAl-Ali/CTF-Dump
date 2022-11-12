from random import randint

flag = "qouybpDa1cm{0ngf4cdn{fc4}pn_4nmeons33tr"

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

for _ in range(100):
    shift = randint(1, len(set(flag)) - 1)
    print(encrypt("qouybpDa1cm{0ngf4cdn{fc4}pn_4nmeons33tr"))
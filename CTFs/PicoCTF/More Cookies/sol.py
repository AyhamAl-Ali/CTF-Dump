#!/usr/bin/python3
import requests
import base64

# CBC-Decrypt

url = "http://mercury.picoctf.net:43275/"

s=requests.Session()
s.get(url)
cookie=s.cookies["auth_name"]
print(cookie)
unb64=base64.b64decode(cookie)
print(unb64)
unb64b=base64.b64decode(unb64)
for i in range (0,128):
   pos=i//8
   guessdec=unb64b[0:pos]+((unb64b[pos]^(1 << (i%8))).to_bytes(1,'big'))+unb64b[pos+1:]
   guessenc1 = base64.b64encode(guessdec)
   guess=base64.b64encode(base64.b64encode(guessdec)).decode()
   r=requests.get(url, cookies={"auth_name": guess})
   if "pico" in r.text:
       print(r.text)
       print("guess: " + guess)

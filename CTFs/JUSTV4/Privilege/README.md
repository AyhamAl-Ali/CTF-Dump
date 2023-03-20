Another amazing chall, **JSON INJECTION** that's nice!

There was a website with `robots.txt` giving us a page with the following info
```
{
  "username":"john",
  "privilege":"admin",
  "pass":"password"
}
```
And we had cookies (base64) and a page that has the flag, we needed to change the cookie `user: admin` and `privilege: admin`

the cookie only contains `user, pass` with their values, I tried to manually add a new json key and value but didn't work, the code wasn't checking for json integrity which means we can do JSON injection

we need to add `"privilege":"admin"` in an unauthorized way, which is how we made the passowrd key with **JSON INJECTION** and send it to login

```
user: john
pass: password","privilege":"admin
```
The play was in either user or pass keys, I chose pass key to be `pass: password","privilege":"admin`
This would be parsed in the backend as
```
{
  "username":"john",
  "privilege":"user",
  "pass":"password"
  "privilege":"admin"
}

```
VOILAAA!! We've admin perms now!

Ref:
https://www.invicti.com/learn/json-injection/

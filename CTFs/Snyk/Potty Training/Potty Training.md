### Potty Training

> Sponsored by stegano
> 
> Attachements: potty.png

### Solution

- First things I did to the image was `binwalk --dd='.*' potty.png` I had some results but all were not useful, broken files

- I then tried the amazing zsteg tool on it using `zsteg -a potty.png` and I had some good results! scrolling up to the beginning I found 

- ```v
  ┌──(ayham㉿AM-Kali)-[~]
  └─$ zsteg -a './potty.png' 
  imagedata           .. text: "-\"\nVD51%"
  b1,r,lsb,xy         .. text: ";R.3Ov?*7.>?&\""
  b1,rgb,lsb,xy       .. text: "111:\n        import requests\n        r = requests.get('http://potty-training.c.ctf-snyk.io/')\n        print(r.text)"
  b2,r,msb,xy         .. text: "]}}wUuUu"
  b2,g,msb,xy         .. text: "u}UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
  b2,b,lsb,xy         .. text: "AUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
  ```

- At output line 3 I found a webpage! open it and got the flag!

- > FLAG: **SNYK{dd67edb70a28335068dd5ea9304007b69543357ff471b3144e3355bca34cb35d}**

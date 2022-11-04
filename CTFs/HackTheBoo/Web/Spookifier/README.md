# Spookifier

> **DIFFICULTY**: easy
> 
> **POINTS**: 200

### Question

> There's a new trend of an application that generates a spooky name for you. 
> Users of that application later discovered that their real names were 
> also magically changed, causing havoc in their life. Could you help 
> bring down this application?

### Solution

- After reading the code and understanding it I saw no direct way of exploitation which then the chall became more interesting!

- I saw template rendering methods and instantly came into my mind that it could be SSTI! so I searched for SSTI payloads and got this [GitHub - payloadbox/ssti-payloads: 🎯 Server Side Template Injection Payloads](https://github.com/payloadbox/ssti-payloads)

- I tested some but failed until I reached this and it worked!!!
  
  ```py
  ${6*6}
  ```

- I am not that good at SSTI tbh and I tried to google it and get to know more about how it really works and found this amazing tool [GitHub - vladko312/SSTImap: Automatic SSTI detection tool with interactive interface](https://github.com/vladko312/SSTImap)

- I ran it and got some outputs saying it's **Mako** engine and the knowns exploits are are marked as **NO** but that's okay

- Now I searched for **Mako SSTI Payloads** and tried to only use payloads that have characters defined in font4 in **utils.py** from the src because that's the only font has some symbols support and symbols like `__` (double underscores) can't be used

- Aaaaaaand I found this payload from [PayloadsAllTheThings/README.md at master · swisskyrepo/PayloadsAllTheThings · GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#mako)

- ```py
  ${self.module.runtime.util.os.system("id")}
  ```

- And it worked!!!

- Now I changed the command 

- ```py
  - ```py
    ${self.module.runtime.util.os.popen("cat /flat.txt".read()}
  ```
  
  ```
  
  ```

- Aaaand VOILAAA!!

- Response was: `HTB{t3mpl4t3_1nj3ct10n_1s_$p00ky!!}}`

### Flag

> HTB{t3mpl4t3_1nj3ct10n_1s_$p00ky!!}}

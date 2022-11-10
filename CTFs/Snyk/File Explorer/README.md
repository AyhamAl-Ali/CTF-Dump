### File Explorer

> Expose hidden files in the web application.
> 
> http://file-explorer.c.ctf-snyk.io/
> 
> Hint: https://github.com/lcrowther-snyk/file-explorer

### Solution

- After looking around in the source code, the README.md says `simple app just using st lib` which made me search `st lib exploit` directly and found a Path Traversal vulnerability at [Directory Traversal in st | CVE-2014-3744 | Snyk](https://security.snyk.io/vuln/npm:st:20140206)

- I tried to do send the payload `http://file-explorer.c.ctf-snyk.io/public/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd` but no response is returned! kept looking around until I thought of encoding the forward slash as well!

- Forward slash encoding code is `%2f` so I tried this payload `http://file-explorer.c.ctf-snyk.io/public/%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F/etc/passwd` and got a response!!

- Now it's time to search for the flag

- I tried to reduce the `../` to reach various places and look around until I found `src` when requesting `http://file-explorer.c.ctf-snyk.io/public/%2E%2E%2F%2E%2E%2F%2E%2E%2F` got inside then found `groof` then inside you will find `flag`!

- ![2022-11-09-18-08-57-image.png](/home/ayham/Github/CTF-Dump/CTFs/Snyk/File%20Explorer/2022-11-09-18-08-57-image.png)

- VOILAAAA!

- > Flag: SNYK{6854ecb17f23afdf2610f741dd07bd6099c616e4ac2a403eb14fa8689e1fb0af}

One of the amazing challs that had a nice idea, it was a file of `54 GB` !!! it was full of "troll" word in each line, the idea was that the flag is at the end of the file

So to get the flag you would need to only download part of the file not all of it ofc :D

And to do that you can use `curl` like this:

`curl -r 44999414784- http://web.hackerspacejust.com:8081/flag.txt | grep -i just` the number was found from trial and error, since we know the file size we need to convert that to bytes and extract some bytes from that for safety and download like 1 mb of the file

FLAG: `JUST{G0t_Wh4t_Y0u_w4nt?}`


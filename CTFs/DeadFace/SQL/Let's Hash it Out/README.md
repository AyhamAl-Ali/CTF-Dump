## Challenge

> Created by: **syyntax**
> 
> DEADFACE discussed what users they were going to target out of the database dump obtained. Look around on [Ghost Town](https://ghosttown.deadface.io) and submit the password hash of the user they are targeting.
> 
> Submit the flag as `flag{hash}`.
> 
> *Use the database from **Counting Heads**.**

We need to filter the following:

- Searching through their forums we found this post `[Database question](https://ghosttown.deadface.io/t/database-question/46)`
- Reading thru their comments we found the needed comment 
- > I mean most of those users are students. Get their data if you can but 
  > just remember we’re not really trying to go after students. They’re 
  > getting ripped off by these schools - we want to punish the 
  > administration, not the students.
- We now know they want the admin's password
- From `roles` table we know admin role = `8`
- From `roles_assigned` table we filter the user of role_id = 8
- From `passwords` table we filter user of user_id that we got from the above filteration
- Congrats

### Solution

> SELECT user_id FROM roles_assigned
> WHERE role_id = 8;
> 
> == 1440
> 
> SELECT password from passwords
> WHERE user_id = 1440;
> 
> == b487af41779cffb9572b982e1a0bf83f0eafbe05

### Answer

`flag{b487af41779cffb9572b982e1a0bf83f0eafbe05}`
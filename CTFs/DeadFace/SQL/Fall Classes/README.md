## Challenge

> Created by: **syyntax**
> 
> How many unique Fall courses are present in the database dump? Submit the flag as `flag{#}`.
> 
> *Use the database from **Counting Heads**.*

We need to filter the following:

- Courses that are in Fall (term_courses.term_id = 2)

### Solution

> SELECT count(*) FROM term_courses
> WHERE term_id = 2;

### Answer

`flag{495}`
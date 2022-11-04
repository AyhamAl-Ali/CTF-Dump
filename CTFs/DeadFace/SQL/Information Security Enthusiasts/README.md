## Challenge

> How many Fall enrollments are there in Information Systems Security (ISSC) courses? Submit the flag as flag{#}.

We need to filter the following:

- Courses that their title begin with "ISSC" `(courses.title like "%ISSC%")`

- Courses that are in Fall `(term_courses.term_id = 2)`

- Entrollments that are in the result of above filtered courses `(enrollments.term_crs_id = term_courses.term_crs_id)`

### Solution

> SELECT * FROM courses, term_courses, enrollments
> WHERE courses.course_id = term_courses.course_id
> AND enrollments.term_crs_id = term_courses.term_crs_id
> AND courses.title like "%ISSC%"
> AND term_courses.term_id = 2;

### Answer

`flag{526}`
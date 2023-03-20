The idea of the chall was to underflow, making a variable reach 0 from 1337 value, we had the code, the idea was to give a value that the var will be multiplied by and that value should be very small but we can't put a 0, with C if you multiply a value by a very low number it would be equal to 0

There was a hint saying something like `1e-10` which is equal to -1 with 10 zeros on the right `-10000000000`

This was the output of the netcat when I was trying to solve it

------------------------------------------
X is the remaining years for the guardian to live !
Can you make X = 0 ??
X = 1337.133700
------------------------------------------
> 1e-11
1.337133699999999931755e-08
------------------------------------------
> 1e-111
1.337133700000000089008e-119
------------------------------------------
> 1e-1111
you power doesn't work this way );
1.337133700000000089008e-119
------------------------------------------
> 1e-11111
you power doesn't work this way );
1.337133700000000089008e-119
------------------------------------------
> 1e-1114 
you power doesn't work this way );
1.337133700000000089008e-119
------------------------------------------
> 1e-111
1.337133700000000136967e-230
------------------------------------------
> 1e-1111
you power doesn't work this way );
1.337133700000000136967e-230
------------------------------------------
> 1e-1110
you power doesn't work this way );
1.337133700000000136967e-230
------------------------------------------
> 1e-111
0.000000000000000000000e+00
------------------------------------------
Well Done, the guardian wasn't that strong after all !!
`JUST{Und3rfl0w_m4gic_w17h_d0ubl3s_387618721234}`

so the idea was to keep multiplying it with `1e-111` until it reaches `0`



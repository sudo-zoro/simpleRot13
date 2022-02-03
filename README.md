## simpleRot13


|0 | 1 | 2 | 3 | 4 | 5  |6  |7  |8  |9  |10 |11 |12| 
|----|----|----|----|----|----|----|----|----|----|----|----|----|
|a | b | c | d | e | f  |g  |h  |i  |j  |k  |l  |m|
|n | o | p | q | r | s  |t  |u  |v  |w  |x  |y  |z|
|13| 14| 15| 16| 17| 18 |19 |20 |21 |22 |23 |24 |25| 

```
abc="abcdefghijklmnopqrstuvwxyz"
cipher="cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
```

 ```
 abc[(abc.find(char)+13)%26]
 
 So lets take
cipher[2] -> p
 
 abc.find(cipher[2])
 abc.find('p') --> index in abc array = 15

 abc[15+13)%26]=abc[2] ==> c
 
 

```

### Arrays in Python 

```python

from array import*
array_name = array(typecode,[initializers])
```
Where typecodes are specific codes for data types 

b	: Represents signed integer of size 1 byte

B	: Represents unsigned integer of size 1 byte

c	: Represents character of size 1 byte

i	: Represents signed integer of size 2 bytes

I	: Represents unsigned integer of size 2 bytes

f :	Represents floating point of size 4 bytes

d	: Represents floating point of size 8 bytes

Initializers are nothing but values assigned.

```python

from array import*
array_name = array('i',[100,90,80,70,60,50])
for x in array_name:
    print(x)
```

Output
```
100
90
80
70
60
50
```



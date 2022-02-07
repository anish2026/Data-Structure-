## Deletion Operation in Array

use remove() function which takes one argument as the element we want to remove

```python

from array import*
array_name = array('i',[100,90,80,70,60,50])
array_name.remove(80)

for x in array_name:
    print(x)
```
Output
```
100
90
70
60
50
```

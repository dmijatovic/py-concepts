# Tips

There are some tips in the py files in this folder. Some tips cannot be put in the code.
These are bellow

## Naming colissions

Take care not to name your module files using the same name as general modules or libraries. This is will create error like this

```python
from flask import *

# IF your module file has name flask to
# this will throw arror because you will be importing
# your module instead of library

```

Same goes for variables named the same as methods in the library

```python
from math import radians, sin

# variable name same as method!!!
radians = radians(90)

rad45 = radians(45)

print(rad45)
```

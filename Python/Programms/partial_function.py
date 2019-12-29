from functools import *
  

def add(a, b, c): 
    return 100 * a + 10 * b + c 

add_part = partial(add, c = 2, b = 1) 
  
print(add_part(3))
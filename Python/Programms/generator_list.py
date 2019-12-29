import time
import sys

def using_generator(n):
    a,b,c=0,1,0
    while c<n:
        yield a
        a,b=b,a+b
        c=c+1            
x=using_generator(20000)

s=time.time()
for i in x:
    pass   
print("generator_time : " ,time.time()-s)
print("genetaror_size : ",sys.getsizeof(x))


l=[]
a=0
b=1 
for i in range(20000):
    l.append(a)
    t=a
    a=b
    b=t+b

s=time.time()
for i in l:
    pass  
print("list_time : " ,time.time()-s)
print("list_size :",sys.getsizeof(l))




    


    
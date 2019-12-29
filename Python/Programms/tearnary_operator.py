a, b = 10, 20
  

min = a if a < b else b   
print(min)


print( (b, a) [a < b] )  

print({True: a, False: b} [a < b])

print((lambda: b, lambda: a)[a < b]())

print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 

min = a < b and a or b 
print(min)
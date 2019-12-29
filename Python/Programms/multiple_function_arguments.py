def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'I', 'am', 'Nikunj') 

def myFun(arg1, **kwargs):
    print ("First argument :", arg1) 
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
myFun("Hi", first ='I', mid ='am', last='Nikunj')     
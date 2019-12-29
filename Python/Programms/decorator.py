def decorator(fun):
    def inner():
        print("Before Function")
        fun()
        print("After function")
    return inner

@decorator
def fun():
    print("In Function")   
#fun=decorator(fun)

fun()
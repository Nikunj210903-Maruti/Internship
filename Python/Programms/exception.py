def divide(x,y):
    try:
        ans=x/y
    except ZeroDivisionError:
        print("error")
    else:
        print("Ans is : ",ans)
    finally:
        print("This always runs")
    

divide(4,2)
print()
divide(4,0)
        

        
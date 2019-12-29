fun=lambda x,y:x+y
print(fun(10,15))

l=[1,2,3,4,5,6,7,8,9]

f_l=list(filter(lambda x:(x%2==0),l))
print(f_l)

m_l=list(map(lambda x:x*2,l))
print(m_l)
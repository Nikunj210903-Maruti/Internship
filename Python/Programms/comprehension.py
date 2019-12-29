l=[1,2,3,4,5,6,7,8,9]

#List Comprehension
c_l=[i for i in l if i%2==0]
print(c_l)

#Generator Comprehension
c_g=(i for i in l if i%2==0)
print(c_g)

#Dictionary Comprehension
c_d={i:i*2 for i in l if i%2==0}
print(c_d)
state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 
c_d = {key:value for (key, value) in zip(state, capital)}
print(c_d) 

#Set Comprehension
c_s = {var for var in l if var % 2 == 0} 
print(c_s)
import pickle
f=open("file.txt","wb")
data='hello'
pickle.dump(data,f)
f.close()

f=open("file.txt","rb")
f_data=pickle.load(f)
print(f_data)
f.close()
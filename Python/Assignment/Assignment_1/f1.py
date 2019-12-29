from urllib.request import urlopen
import json
import csv

def clean():
    for i in items:
        if i["stargazers_count"]>2000:
            di={"name":i["name"],"description":i["description"],"html_url":i["html_url"],"watchers_count":i["watchers_count"],"stargazers_count":i["stargazers_count"],"forks_count":i["forks_count"]}
            cleaned.append(di)
      
link="https://api.github.com/search/repositories?q=is:public+forks:>=200+language:Python"
f=urlopen(link)
data=json.loads(f.read())

if data:
    print("Data Received Successfully!!")
    print()
    items=data["items"]
    no_of_items=len(data["items"])
    print("There are %d items in unfiltered data"%(no_of_items))
    print()
    
    if no_of_items>0:
        cleaned=[]
        clean()
        
    else:
        print("There are no items to filter")
        
    file=open("cleaned.csv","w")

    if len(cleaned)>0:
        print("Filtered Items : ", len(cleaned))
        print()
        print(cleaned)
        print()
        if file:
            keys=cleaned[0].keys()
            dict_writer=csv.DictWriter(file,keys)
            dict_writer.writeheader()
            dict_writer.writerows(cleaned)
            print("Data are writen in file successfully!!")
            print()
        else:
            print("Failed to write filtered data in file")
            print()
        
    else:
        print("There are no item that satisfy the condition")
    
    file.close()
        
else:
    print("No data found")
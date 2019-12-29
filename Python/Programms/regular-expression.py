import re

string="123 hello 123 nikunjbhai 210903"
m=re.findall(r'[a-z]+',string)
print(m)

m=re.match(r'[a-z]+',string)
print(m)

m=re.search(r'[a-z]+',string)
print(m)

m=re.sub(r'[a-z]+',"",string)
print(m)
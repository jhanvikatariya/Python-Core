book={}
book['naitik']={'name':'naitik','address':'ahmedabad','contact':99999999}
book['vishwa']={'name':'vishwa','address':'ahmedabad','contact':00000000}

import json
s=json.dumps(book)
print(type(s))
print(s)

# when with is used while opening a file it does not need to be closed but it closes it self when file using is over
with open('new.txt','w') as f:
    f.write(s)
with open('new.txt','r') as f:
    p=f.read()
    print(p)
    
import json
s1=json.loads(s)
print(type(s1))
print(s1)
print(book['naitik'])
print(book['naitik']['contact'])
for i in book:
    print(book[i])
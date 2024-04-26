l1=[10,20,30,40,50,60,70,80,90]
s=0
for i in l1:
    s+=i
print(s)

n="Techno IT hub"
for i in n:
    print(i)
    
for i in range(11):
    print(i)
    
for i in range(2,11):
    print(i, end=" ")
'''    
l = [1,2,3,4,5,6,7,8,9,10,11,12]
l2 = ["jan","feb","march","april","may","june","july","august",'sep',"oct","nov","dec"]
s=0
for i in l:
    r = l[s]
    s+=1
for j in l2:
        print(l[r],l2[r])'''

ex = [100,200,300]    
total = 0
for i in range(len(ex)):
    print("month: ",i,"expences",total)
    total = total+ex[i]
print(total)

key_loc = 'chair'
loc = ['stool','bench','table','chair','living room']
for i in loc:
    if i==key_loc:
        print("key found in ",i)
        break
    else:
        print("key not found",i)
        
for i in range(0,11,2):
    print(i)
    
count=0
while (count<11):
    if count%2==0:
        print(count)
    count+=1
    
count=10
while (count>=0):
    if count%2==0:
        print(count)
    count-=1
    
i=100
while True:
    print(i)
    if i%10==0:
        break
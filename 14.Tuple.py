#tuple
t=(1,2,3,4,5,2,3)
print(t)
print(t[0])

#tuple[0]=10 #not allowed
t1=(1,1.5,'hello',None,True)
print(t1)

print("Len ", len(t))
print("slice 0 - 2 ",t[0:2])
print("slice 1 - n",t[1:])
print("slice i to 2", t[:2])

print("concat",t+t1)
print("count" ,t.count(1))
print("index", t.index(2))
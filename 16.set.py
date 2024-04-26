#sets

s={1,2,3,4,1}
print(s)

s1={'a',2,2,3,None,True}
print(s1)

for value in s1:
    print(value)
    
#union

s1={1,2,3,4,5}
s2={5,6,7}
print('union',s1.union(s2))
print('intersection ',s1.intersection(s2))
print('symmetric difference:',s1.symmetric_difference(s2))
print('difference: ',s1.difference(s2))

s3={1,2}
s4={3}
print('is disjoint:',s3.isdisjoint(s4))

s5={1,2}
s6={1}
print('is superset',s5.issuperset(s6))
print('is subset',s5.issubset(s6))
s7={1,2}
s7.remove(2)
print(s7)
print(s7.discard(3))
s8={1,2,3}
s8.pop()
print("pop",s8)
s9={1,2,3}
del s9
s10={1,2,3}
s10.clear()
print("clear",s10)
if i in s1:
    print(True)
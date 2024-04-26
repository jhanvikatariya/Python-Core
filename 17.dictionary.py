dic={"Name":"Techno IT Hub","Sector":"EdTech"}
print(dic)
print("Name: ",dic["Name"])
print("Get Method: ",dic.get("Sector"))
print("keys:",dic.keys())
for keys,values in dic.items():
    print("keys",keys)
    print("value",values)
    
print("values", dic.values)
ep1={1:3,2:4}
ep2={1:2,3:4}
ep1.update(ep2)
print(ep1)

ep1.clear()
print(ep1)
ep2.pop(1)
print(ep2)
ep2={1:2,3:4}
ep2.popitem()
print(ep2)
del ep1
del ep2[1]
print(ep2)
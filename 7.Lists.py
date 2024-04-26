L1=["Shubman", "Virat", "Rohit", "Sachin"]
print(L1)

L2=["Virat", 10, 10.5]
print(L2)

print(L1[0])
print(L1[-1])

print("Length ", len(L1))

print("Slicing ", L1[1:2])
print("Slicing ", L1[1:])
print("Slicing ", L1[:2])
print("Slicing ", L1[0:3:2])

L3=[i*i for i in range(10)]
print(L3)

L4=[i*i for i in range(10) if i%2==0]
print(L4)

L5=[10,2,5,710,50]
L5.sort()
print("Sorted List ", L5)

L1.append("Shubman")
print("Appended List ", L1)

L5.sort(reverse=True)
print("Reversed Sorted List", L5)

L1.pop(2)
print("List after pop ", L1)

print("Index", L1.index("Shubman"))

print("Count", L1.count("Shubman"))

L6=L1.copy()
print("Copy", L6)

L1.insert(4,"Ishan")
print("Insert ", L1)

L7=L1+L6
print("Concatenate ", L7)

L2.extend(L3)
print("Extend ", L2)

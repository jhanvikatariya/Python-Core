l1 = [1,2,3]
l2=[4,5,6]

total = 0
for i in l1:
    total+=i
print("l1",total)

total = 0
for i in l2:
    total+=i
print("l2",total)

def amt(l3):
    total = 0
    for i in l3:
        total+=i
    return total

ltotal1=amt(l1)
ltotal2=amt(l2)

print(ltotal1)
print(ltotal2)

def add(a=20,b=10):
    print("default",a+b)
add(b=10,a=20)


def add(a,b=10):
    print("require",a+b)
add(a=20)

def add(a,b):
    print("keyword",a+b)
add(a=20, b=10)

def add(*a):
    for i in a:
        print(a)
add(10,5,20)

def add(**a):
    for i in a:
        print(a['fname'], a['lname'])
add(fname = "techno",lname='hub')
#function without argument and without runtype

def add():
    print("abg")
add()

#function with argument and without runtype

def add(a,b):
    print("abg",a,b)
add(1,2)

#function without argument and with runtype

def add():
    return ('asdf')
a=add()
print(a)

#function with argument and with runtype

def add(b):
    return ('asdf',b)
a=add(10)
print(a)
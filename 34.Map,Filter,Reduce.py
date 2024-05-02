#without map
def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,4,6,4,3]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)


#with map
# def cube(x):
#     return x*x*x
# print(cube(2))
# l=[1,2,4,6,4,3]
# newl=[]
# newl=list(map(cube,l))
# print(newl)


def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,4,6,4,3]
newl=[]
newl=list(map(cube,l))
print(newl)


#filter
def filter_function(a):
    return a>2
newnewl=list(filter(filter_function,l))
print(newnewl)

#reduce
from functools import reduce
numbers=[1,2,3,4,5]
sum1=reduce(lambda x,y:x+y,numbers)
print(sum1)

#is vs ==
a=4
b='4'
print(a is b)
print(a==b)

a={1,2,3}
b={1,2,3}
print(a is b)
print(a==b)

a=3
b=3
print(a is b)
print(a==b)

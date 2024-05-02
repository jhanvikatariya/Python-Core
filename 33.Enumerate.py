#enumerate function 
marks=[10,20,30,40]
for index,mark in enumerate(marks):
    print(index,mark)
    if index==3:
        print('techno it hub')
        

#lambda function
double=lambda x:x*2
print(double(5))

avg=lambda x,y,z:(x+y+z)/3
print(avg(3,5,10))

def apple(fx,value):
    return (6+fx(value))
print(apple(lambda x:x*x*x,2)) 

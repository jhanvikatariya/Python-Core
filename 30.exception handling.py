#without exception  handling ,try to enter string
a=input('enter number: ')
print('multiplication:')
for i in range(11):
    print(f'{int(a)}x{i}={int(a)*i}')
print('some lines')    

#with exception handling ,try to enter string 
a=input('enter number: ')
print('multiplication: ')
try:
    for i in range(11):
        print(f'{int(a)}x{i}={int(a)*i}')
except:
    print('invalid input')
print('some lines')

#pre defined exceptions
try:
    num=int(input("enter number"))
    a=[6,3]
    print(a[num])
except ValueError:
    print('enter integer')
except IndexError:
    print('index error')
    
    
#finally block
try:
    l=[1,5,6,7]
    l=int(input('enter index:'))
    print(l[i])
except:
    print('some error')
finally:
    print('i am always executed')  
    
def fun():
    try:
        l=[1,2,3]
        i=int(input('Enter index:'))
        print(l[i])
        return 1 
    except:
        print('some error')
        return 0
    finally:
        print("executed")
        
x=fun()
print(x)


#raising custom error

a=int(input("enter number:"))
try:
    if a<5 or a>9:
        raise ValueError('value should be between 5 and 9')
except ValueError as v:
    print(v)

a=int(input())
if(a>18):
    print("Eligible to drive")
    
a=int(input())
if(a%2==0):
    print("Even")
else:    
    print("Odd")
    
a=int(input())
if(a>0):
    print("Positive")
elif(a==0):
    print("Zero")
else:
    print("Negative")
    
North=['daal', 'rice', 'chole','kulcha']
South=['idli','dosa','sambhar']
a=input("Enter food:")
if a in North:
    print("North Indian Food")
elif a in South:
    print("South Indian food")
else:
    print("Item not in the list")
    
a=int(input("Enter numbers between 1 to 24"))
if a in range(1,12):
    print("good morning")
elif a in range(13,24):
    print("good evening")
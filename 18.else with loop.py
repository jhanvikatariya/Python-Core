for i in range(5):
    print(i)
    
else:
    print('sorry')
    
i=0
while(i<5):
    print(i)
    i+=1
else:
    print('sorry')
    
#here else will not print 
i=0
while(i<5):
    print(i)
    i+=1   
    if i==5:
        break
else:
    print('sorry')
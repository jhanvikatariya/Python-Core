
#ITHOUSE
import time
print(time.time())

def usingWhile():
    i=0
    while i<0:
        i+=1
        print(i)

def usingFor():
    for i in range(10):
        print(i)
        
init=time.time()
usingFor()

t1=time.time()-init
init=time.time()

usingWhile()

print(time.time()-init)
print(t1)

print(10)
time.sleep(5)
print('After 5 second')

import time
t=time.localtime()
f_time=time.strftime('%Y-%m-%d %H-%M-%S',t)
print(f_time)
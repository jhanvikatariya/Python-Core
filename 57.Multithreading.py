#multithreading
import threading
import time
def func(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
time1=time.perf_counter()

t1=threading.Thread(target=func,args=[15])
t2=threading.Thread(target=func,args=[13])
t3=threading.Thread(target=func,args=[10])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2=time.perf_counter()
print(time2-time1)


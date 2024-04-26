#factorial and recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print("Factorial",fact(3))

#fibonacci and recursion
def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(6):
    print(fibonacci(i),end="")

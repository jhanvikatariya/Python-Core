def greet(func):
    def one(*args,**kwargs):
        print('Good Morning')
        func(*args,**kwargs)
        print('Thanks')
    return one

@greet
def hello():
    print('hello')
def add(a,b,c):
    print(a+b+c)
    
hello()
greet(add)(1,2,3)
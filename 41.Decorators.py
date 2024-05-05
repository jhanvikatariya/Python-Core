#Decorators

def greet(func):
    def one():
        print('Good Morning')
        func()
        print('Thanks')
        return one
    one()

def hello():
    print('Hello')

hello=greet(hello)

@greet
def hi():
    print('Hi')
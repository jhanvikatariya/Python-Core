#Constructor

#Default Constructor
class Person:
    def __init__(self):
        print('Hello')
a=Person()


#Parameterized Constructors
class Person2:
    def __init__(self,n,o):
        self.name=n
        self.occ=o
        print(f'{self.name} is {self.occ}')
a=Person2('Rachin', 'GET')
b=Person2('Shanti','SE')
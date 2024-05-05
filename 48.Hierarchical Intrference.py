class Parent:
    def __init__(self,a):
        self.cmd=a
    def Sub(self):
        print(f'This is parent class for {self.cmd}')
        
class Child1(Parent):
    def __init__(self,a):
        self.cmd=a 
        
class Child2(Parent):
    def __init__(self,a):
        self.cmd=a
        
ch1=Child1('George')
ch2=Child2('Sam')
ch1.Sub()
ch2.Sub()
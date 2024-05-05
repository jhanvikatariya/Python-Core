#Public

class student:
    def __init__(self,age,name):
        self.age=age
        self.name=name
obj=student(21,'Rachin')
print('Age of Public', obj.age)
print('Name of Public', obj.name)


#Private
class employee:
    def __init__(self):
        self.__name='Harry'
        
a=employee()
#print (a.__name) 

class MyClass:
    def __init__(self):
        self._private_attribute='Private'
        self._mangled_attribute='Mangled'
my_object=MyClass()
print('Private Object:', my_object._private_attribute)

#print(my_object._mangled_attribute)
print('Mangled Object', my_object._mangled_attribute)


#Protected

class student:
    def __init__(self):
        self._name='Rachin'
    def _funname(self):
        return 'TIH'

class subject(student):
    pass

obj=student()
obj1= subject()

print(obj._name)
print(obj._funname())

print(obj1._name)
print(obj1._funname())
class Database:
    def __init__(self,n,id):
        self.name=n
        self.id=id
    def Result1(self):
        print(f'{self.name} has id {self.id}')
class Database2(Database):
    def __init__(self,n,id,s):
        self.name=n
        self.id=id
        self.salary=s
    def Result2(self):
        print(f'Employee is paid {self.salary}')
class Employee(Database2):
    def __init__(self,n,id,s):
        self.name=n
        self.id=id
        self.salary=s
    def Result3(self):
       print('These are the employee details')
emp=Employee('Harry',234,22)
emp.Result1()
emp.Result2()
emp.Result3()
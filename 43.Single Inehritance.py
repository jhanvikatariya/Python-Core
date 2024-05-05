#Single 
class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f'{self.name} have {self.id} as id')
        
class programmer(employee):
    def showLanguage(self):
        print('Python')

e1=employee('Shanti Vyas',400)
e1.showDetails()
e2=programmer('Rachin rathod', 200)
e2.showDetails()
e2.showLanguage()
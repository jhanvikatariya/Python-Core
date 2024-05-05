class Employee:
    def __init__(self, name):
        self.n=name
    
    def __len__(self):
        return len(self.n)
    
e=Employee('Rachin')
print(e.n)
print(len(e))
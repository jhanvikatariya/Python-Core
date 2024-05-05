class Person:
    Company='Techno IT Hub'
    Sector='Edtech'
    def info(self):
        print(f'{self.Company} is an {self.Sector} company')
a=Person()
b=Person()
a.info()

b.Company='Amprow'
b.Sector='Digital'
b.info()
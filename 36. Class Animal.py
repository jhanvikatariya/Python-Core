class Animal:
    def __init__(self,w,r,n,e):
        self.walk=w
        self.run=r
        self.name=n
        self.eat=e
    def do_work(self):
        if self.walk=='fast':
            print(self.name,'is',self.run)
            
        elif(self.walk=='slow'):
            print(self.name,'is',self.run)
            
    def eating(self):
        if self.eat=='bone':
            print(self.name,'is eating',self.eat)
        elif self.eat=='meat':
            print(self.name,'is eating',self.eat)
        
puppy=Animal('fast','running','Siberian Husky','meat' )
puppy.do_work()
puppy.eating()
puppy2=Animal('slow','walking' ,'Pomeranian','bone')
puppy2.do_work()
puppy2.eating()
class Human:
    def __init__(self,n,o,a):
        self.name=n
        self.occupation=o
        self.age=a
        
    def do_work(self):
        if self.occupation=='tennis player':
            print(self.name,'plays tennis')
            
        elif(self.occupation=='actor'):
            print(self.name, 'shoots film')
        print(self.age)
    def speaks(self):
        print(self.name,'says how are you?')
        
tom=Human('tom cruise','actor',24 )
tom.do_work()
tom.speaks()

maria=Human('maria sharapova', 'tennis player',19)
maria.do_work()
maria.speaks()

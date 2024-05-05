import random
class Game:
    def __init__(self,c,n):
        self.comp=c
        self.num=n
    def Result(self):
            if(self.num==0 and self.comp==1):
                print('You win')
            elif(self.num==1 and self.comp==2):
                print('Computer wins')
            elif(self.num==0 and self.comp==2):
                print('You win')
            elif( self.num==2 and self.comp==0 ):
                print('Computer wins')
            elif( self.num==2 and self.comp==1 ):
                print('You win')
            elif( self.num==1 and self.comp==0 ):
                print('Computer wins')
            else:
                print('It is a tie')
n=int(input('Enter your choice(0/1/2):'))
c=random.randint(0,2)
game=Game(c,n)
print(c)
game.Result()

            
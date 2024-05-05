#Walrus operaator
#the walrus operator, denoted by :=, assigns values to variables ad part of an expression. It's particularly useful for assignments within expressions, eliminating the need for rebundant lines. Let's go through your examples:
A=True
print(A:=False)

numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())
    
happy=True
print(happy)
print(happy:=False)

foods=list()
while True:
    food=input('What food do you like?:')
    if food=='quit':
        break
    foods.append(food)
    
print(foods)

foods=list()
while(food:=input('What food do you like?: ')!='quit'):
    foods.append(food)
print(foods)
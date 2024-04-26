'''this is a program containing docs string'''
def square(n):
    '''take n numbers and return square of the n'''
    print(n**2)
square(5)
print(square.__doc__)

#formatted string

letter= "hello, welcome to {},name{}"
company= "techno it hub"
name ='xyz'
print(letter.format(company,name))

#index based formatted string

letter= "hello {1},welcome to ,name{0}"
name ='xyz'
company= "techno it hub"
print(letter.format(company,name))

print(f'hello {name},welcome to {company}')
print(f"{10*20}")
print(f"{{name}}")
a = 10.34383
print(f"{a}")
print(f'{a:2f}')
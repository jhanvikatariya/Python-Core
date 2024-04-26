x=4
print('local x:',x)
def hello():
    x=5
    print(f'local in hello{x}')
print(f'globL X OUTSIDE HELLO IS {x}')
hello()

print(f'global x outside hello after calling hello is{x}\n\n\n')

y=4 
print('local y:',y)
def hello():
    global y 
    y=5
    print(f'local in hello {y}')
print(f'global y outside hello is {y}')
hello()
print(f'global y outside hello after calling hello {y}')


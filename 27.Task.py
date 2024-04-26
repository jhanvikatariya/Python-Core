n=input('Enter any string:')

def encrypt():
    a='abc'
    x='xyz'
    c=a+n[1:]+n[0]+x
    print(c)

def decrypt():
    name=n[3:]
    c=name[-4]+name[:-4]
    print(c)
    
choice=input("Do you want to encrypt or decrypt your name?? ")
choice.lower()
if choice=='encrypt':
    encrypt()
elif choice=='decrypt':
    decrypt()
else:
    print('enter valide choice')
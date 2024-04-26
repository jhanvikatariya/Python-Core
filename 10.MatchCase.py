x=int(input("Enter number"))
match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case _:
        print("Greater than one")
        
x=input("Enter choice: ")
a,b=10,20
match x:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("Invalid Case655")
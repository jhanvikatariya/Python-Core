quiz_list=[['Which of this is the national fruit?', 'a.apple', 'b.orange', 'c.mango','c' ], ['Which of this is the national bird?', 'a.Peacock', 'b.Crow', 'c.Parrot', 'a']]
for i in range(0,len(quiz_list)-1):
    print(quiz_list[i][0])
    print(quiz_list[i][1],'\n', quiz_list[i][2],'\n',quiz_list[i][3])
    result=input('Enter your answer choice: ')
    result.lower()
    if (result==quiz_list[i][4]):
        print('Your answer is right')
        print(quiz_list[1][0])
        print(quiz_list[1][1],'\n', quiz_list[1][2],'\n',quiz_list[1][3])
        result1=input("ENter your answer choice: ")
        result1.lower()
        if (result1==quiz_list[i+1][4]):
            print('right')
            break
    else:
        break
# print(quiz_list[0][0])
# print(quiz_list[0][1],'\n', quiz_list[0][2],'\n',quiz_list[0][3])
# result=input("Enter the correct choice from the options: ")
# result.lower()
# if (result==quiz_list[0][4]):
#     print("Your 1st answer is correct")
#     print(quiz_list[1][0])
#     print(quiz_list[1][1],'\n', quiz_list[1][2],'\n',quiz_list[1][3])
#     result1=input("Enter the correct choice from the options: ")
#     result1.lower()
#     if (result1==quiz_list[1][4]):
#         print("Your both answers are right")
# else:
#     print("Wrong answer")

    
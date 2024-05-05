# #regular expression
# import re
# pattern='was'
# text='cyclone was good,it has great impact'
# match=re.search(pattern,text)
# print(match)

# import re
# pattern= r'[A-Z]yclone'
# text='Cyclone Dyclone was good'
# matches=re.finditer(pattern,text)
# for match in matches:
#     print(match)
#     print(match.span())
#     print(text[match.span()[0]:match.span()[1]])
import re
# pattern= r'[7-9]234567890'
# pattern=r'\d(?=\d{9})'
pattern=r'[6789](?=\d{9})'
number='9234567890 7654309234 5678345692 ggggggg'
matches=re.finditer(pattern,number)
for match in matches:
    print(match)
    print(match.span())
    print(number[match.span()[0]:match.span()[1]])
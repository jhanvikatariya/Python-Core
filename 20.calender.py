import calendar
cal=calendar.month(2023,9)
print(cal)
#print('leap year:',calendar.isleap(2023))
if (calendar.isleap(2023)!=True):
    print("You are an April fool")
else:
    print("You are not an April fool, but you are a big one")
print('all calendar function:',dir(calendar))

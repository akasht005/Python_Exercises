import calendar

y = int(input("Enter a year : "))

if calendar.isleap(y):

    print("Leap year...")

else:

    print("not a leap year")
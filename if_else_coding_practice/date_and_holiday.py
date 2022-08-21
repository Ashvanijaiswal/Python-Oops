month=input("Enter month name:")
day=int(input("Enter day:"))
if month.capitalize()=='January' and day==1:
    print("Happy new Year")
elif month.capitalize()=='July' and day==1:
    print("Canada day")
elif month.capitalize()=='December' and day==25:
    print("Chrismas day")
else:
    print("Not a fixed date holiday")

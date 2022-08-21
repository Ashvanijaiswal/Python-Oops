feet=float(input("Enter distance in feet:"))
inches=feet*12
yards=2.54*inches/100*1.09
miles=2.54*inches/100/1.6/1000
print(inches,yards,miles,end='\n')
print("%.2f"%inches)
print("%.2f"%yards)
print("%.2f"%miles)

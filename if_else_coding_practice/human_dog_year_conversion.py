dyear=10.5/2
dyear_after=4
hyear=float(input("Enter human year:"))
if(hyear<=2):
    ryear=dyear*hyear
else:
    ryear=10.5 + dyear_after*(hyear-2)
print("dog year will be:",ryear)

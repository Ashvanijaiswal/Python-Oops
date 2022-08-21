grade=input("Enetr Student grade:")
if 'A+'==grade:
    	points=4.0
elif 'A'== grade:
    	points=4.0
elif 'A−'== grade:
    	points= 3.7
elif 'B+'== grade:
    	points= 3.3
elif 'B'== grade:
    	points=3.0
elif 'B−'== grade:
    	points= 2.7
elif 'C+'== grade:
    	points= 2.3
elif 'C'== grade:
    	points=2.0
elif 'C−'== grade:
    	points= 1.7
elif 'D+'== grade:
    	points= 1.3
elif 'D' == grade:
    	points=1.0
else :
        points=0
print(f'grade {grade} point is %.2f'%points)

date=input("Enter month and day:").split(' ')
month=date[0].capitalize()
day=int(date[1])
if month in ['April','May']:
    season='spring'
elif (month=='march' and day>=20) or (month=='June' and day<21):
    season='spring'
elif month in ['July','August']:
    season='summer'
elif (month=='June' and day>=21) or (month=='September' and day<22):
    season='summer'
elif month in ['October', 'November']:
    season='fall'
elif (month =='September' and day>=22) or (month=='December' and day <21):
    season='fall'
else:
    season='winter'
print(f"date {month,day} is in {season}")

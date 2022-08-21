import json

f=open('employee.json','r')
data=json.load(f)
for i in data['accounting']:
    # with open('result.txt','a+') as r:
        # r.write(f"{i['age'],'-',i['firstName'],'-',i['lastName'],'-',i['gender'],'-',i['number']}")
        # r.write('\n')
    # print(i['age'],'-',i['firstName'],'-',i['lastName'],'-',i['gender'],'-',i['number'])
    print(i['firstName']+' '+i['lastName'])

f.close()
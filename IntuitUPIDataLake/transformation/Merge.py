import json
res=""

"""
{
	"a" : 1,
	"b" : {
		"b1" : [1, 2, 3],
		"b2" : "string",
		"b3" : {
			"b31" : true
		}
	},
	"c" : [
		{
			"c01" : "val2",
			"c02" : 8.53
		},
		{
			"c01" : "val2",
			"c02" : 8.53
		}
	]
}
"""

def warpper(sting_json):
    json_obj=json.loads(sting_json)
    res=parse_json(json_obj,"")

def parse_json(json_obj, prevKey=""):

    for key in json_obj:
        if(type(json_obj[key])=='dict'):
            parse_json(json_obj[key], prevKey+"_"+key)
        else:
            if(prevKey==""):
                res = res + key + ":" + json_obj[key]+","
            else:
                res=res+prevKey+"_"+key+":"+json_obj[key]+","

    return "{"+res+"}"


#
df1 , df2

df1.union(df2).withColum().where(rw=1)



{
 "_id": "679216b7560bfbb125391951",
 "index": 0,
 "guid": "4edfe9df-6b1a-4e7f-94aa-1273be7f173b",
 "isActive": true,
 "balance": "$3,705.78",
 "picture": "http://placehold.it/32x32",
 "age": 21,
 "eyeColor": "green",
 "name": "Mosley Cooley",
 "gender": "male",
 "company": "BIZMATIC",
 "email": "mosleycooley@bizmatic.com",
 "phone": "+1 (932) 514-3756",
 "address": "443 Seigel Court, Seymour, New Jersey, 6005",
 "about": "Aute nulla sunt mollit anim qui exercitation id. Amet dolor amet aliqua occaecat eu officia officia veniam laborum. Laboris et irure aute labore anim ex consectetur consequat consectetur nulla sunt voluptate. Adipisicing nulla anim ipsum laboris non elit velit id. Velit nulla nostrud ex irure amet. Duis id ut occaecat minim est consectetur tempor nostrud officia quis.\r\n",
 "registered": "2020-05-06T01:43:56 -06:-30",
 "latitude": -23.279685,
 "longitude": -103.377359,
 "tags": [
   "excepteur",
   "laborum",
   "labore",
   "velit",
   "dolor",
   "quis",
   "cillum"
 ],
 "friends": [
   {
     "id": 0,
     "name": "Jessie Powers"
   },
   {
     "id": 1,
     "name": "Katina Mathews"
   },
   {
     "id": 2,
     "name": "Horn Goff"
   }
 ],
 "greeting": "Hello, Mosley Cooley! You have 9 unread messages.",
 "favoriteFruit": "strawberry"
}





{
	"a" : 1,
	"b" : {
		"b1" : [1, 2, 3],
		"b2" : "string",
		"b3" : {
			"b31" : true
		}
	},
	"c" : [
		{
			"c01" : "val2",
			"c02" : 8.53
		},
		{
			"c01" : "val2",
			"c02" : 8.53
		}
	]
}


{
	"a" : 1,
	"b_b1" : [1, 2, 3],
	"b_b2" : "string",
	"b_b3_b31" : true,
	"c" : [
		{
			"c01" : "val2",
			"c02" : 8.53
		},
		{
			"c01" : "val2",
			"c02" : 8.53
		}
	]
}



--------

def parse_json(json):



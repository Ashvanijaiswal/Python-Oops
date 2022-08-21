from math import sin, cos, sqrt, atan2, radians
R = 6373.0
lat1= radians(float(input("latitude1:")))
long1=radians(float(input("logitude1")))
lat2= radians(float(input("latitude2")))
long2=radians(float(input("longitude2")))
dlon = long2 - long1
dlat = lat2 - lat1
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c=2*atan2(sqrt(a),sqrt(1-a))
distance=R*c
print("distance is:",distance,'km')

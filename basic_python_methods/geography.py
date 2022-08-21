import geopy.distance

coords_1 = (18.937464, 72.898461)
coords_2 = (18.375379, 73.777954)

print geopy.distance.vincenty(coords_1, coords_2).km

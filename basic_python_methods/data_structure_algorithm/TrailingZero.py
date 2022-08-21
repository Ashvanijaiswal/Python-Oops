def num_of_tzero(n:int):
    count:int=0
    i:int=5
    while(i<=n):
        count+=n//i
        i*=5
    return count

print(num_of_tzero(251))

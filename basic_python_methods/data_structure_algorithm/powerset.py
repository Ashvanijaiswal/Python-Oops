
def powerSet(s,i,curr):
    if(i==len(s)):
        print(curr)
        return curr
    powerSet(s,i+1,curr+s[i])
    powerSet(s,i+1,curr)







s='abcd'
powerSet(s,0,"")

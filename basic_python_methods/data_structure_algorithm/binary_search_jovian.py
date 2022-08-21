import time
# def test_location(cards,query,mid):
#     mid_number=cards[mid]
#     if(mid_number==query):
#         if(mid_number==cards[mid-1]):
#             return 'left'
#         else:
#             return 'found'
#     if(mid_number>query):
#         return 'left'
#     else:
#         return 'right'

def locate_card(cards,query):
    lo,hi=0,len(cards)-1
    # nested function
    def test_location(cards,query,mid):
        mid_number=cards[mid]
        if(mid_number==query):
            if(mid_number==cards[mid-1]):
                return 'left'
            else:
                return 'found'
        if(mid_number>query):
            return 'left'
        else:
            return 'right'

    while(lo<=hi):
        mid=(lo+hi)//2
        result=test_location(cards,query,mid)
        if(result=='found'):
            return mid+1
        elif(result=='left'):
            hi=mid-1
        elif(result=='right'):
            lo=mid+1
    return -10

cards=list(range(1,100000,1))
query=300
time1=time.time()
print(time1)
print(locate_card(cards,query))
time2=time.time()
print(time2)
print(time2-time1)

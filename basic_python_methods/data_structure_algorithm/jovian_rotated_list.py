def algorithm(nums,target):

    def binary_search(nums,target):
        lo = 0
        hi = len(nums)-1
        while (lo<=hi):
            mid = (lo+hi)//2
            mid_number = nums[mid]


            if mid > 0 and nums[mid-1]>nums[mid]:
                if(mid<hi and nums[mid]>nums[mid+1]):
                    return hi

                # The middle position is the answer
                return mid

            elif nums[mid]<nums[hi]:
                # Answer lies in the left half
                hi = mid - 1

            else:
                # Answer lies in the right half
                lo = mid + 1

        return 0
    mid=binary_search(nums,target)
    nums_new=nums[mid:]+nums[:mid]
    print(nums_new)

    def searching(nums_new,target):
        low,high=0,len(nums_new)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums_new[mid]==target):
                return mid

            if(nums_new[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return -1
    if(searching(nums_new,target)==-1):
        return -1
    return searching(nums_new,target)

nums=[3,1]
target=3
print(algorithm(nums,target))

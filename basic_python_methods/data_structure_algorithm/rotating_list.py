def count_rotations_linear(nums):
    position = 0                 # What is the intial value of position?

    while position<len(nums)-1:                     # When should the loop be terminated?

        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position >= 0 and nums[position]>nums[position+1]:  # How to perform the check?
            if(len(nums)>2 and nums[position+1]>nums[position+2]):
                return len(nums)-1
            return position+1

        # Move to the next position
        position += 1

    return -1
print(count_rotations_linear([10, 9]))

import numpy as np

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Strategy: 
            1 Calc the cutoff point as the length minus number of desired rotation
            2 Slice the list into 2 lists along the cutoff point
              2.1 Flip the end list that needs rotating during slicing
            3 Replace nums w/a copy of it with the starting + ending lists in the opposite order
        """
        
        numsCount = len(nums)
        
        #if rot same number as list length
        if( k == numsCount):
            #don't needa change arr
            return
        
        #if rot more than a full swap
        if( k > numsCount):
            k = k % numsCount
        
        rotateShiftCutoff = numsCount-k
        
        #arr slicing is non-inclusive
        
        #rot #'s cutoff to one before count
        rotatedNums = nums[rotateShiftCutoff:numsCount]
        
        #shift #'s 0 to one before cutoff
        shiftedNums = nums[0:rotateShiftCutoff]
        
        #concat rotated to shifted nums to COPY of nums
        nums[:] = rotatedNums + shiftedNums
        
        print(nums)

nums = [1,2,3,4,5,6,7]

Solution.rotate(self=Solution, nums=nums, k=3)

print(nums)
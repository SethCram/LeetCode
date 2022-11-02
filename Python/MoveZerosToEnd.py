class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Was likely supposed to use 2 pointers and then compare their vals for swapping, but easier just to make a new list.
         "Note that you must do this in-place without making a copy of the array."
        """
        
        #remove all zeros from list
        # List comprehension creates a new list from an existing list, or creates what is called a sublist.
        #nums[:] = (value for value in nums if value != 0)
        
        numOfZeros = 0
        newList = []
        
        #walk thru list
        for currNum in nums:
            #if not 0
            if currNum != 0:
                #add to new list
                newList.append(currNum)
            #if zero
            else:
                #incr 0 count
                numOfZeros += 1
        
        #while still zeros to add
        while( numOfZeros > 0 ):
            #add zero + decr 0 counter
            newList.append(0)
            numOfZeros -= 1
            
        #copy over new list to passed in list
        nums[:] = newList
        
        print(nums) 
        
    def moveZeroes(self, nums):
        """
            type nums: List[int]
            rtype: void Do not return anything, modify nums in-place instead.
        """
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count

nums = [0,1,0,2,3,4,5,6,7]

Solution.moveZeroes(self=Solution, nums=nums)

print(nums)
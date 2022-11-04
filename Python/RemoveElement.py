class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Instructions: 
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

        Return k after placing the final result in the first k slots of nums.

        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

        Double pointer approach.
        Speed: O(N)
        Space: O(1)
        """
        
        numsLen = len(nums)
        
        ptr1 = 0
        ptr2 = 0
        
        valsFound = 0
        
        for ptr1 in range(numsLen):
            #if num at ptr 1 is val and no vals found yet
            if nums[ptr1] == val and valsFound == 0:
                #place pointer 2 at curr val
                ptr2 = ptr1
                valsFound += 1
                #advance ptr1
                ptr1 += 1
            #if num at ptr1 is val and a starting pnt for pntr2 found
            elif nums[ptr1] == val:
                ptr1 += 1
                valsFound += 1
            #if num at ptr1 isn't val 
            elif nums[ptr1] != val:
                #copy ptr1 num to ptr2 num
                nums[ptr2] = nums[ptr1]
                #advance both pointers
                ptr1 += 1
                ptr2 += 1
        
        return numsLen - valsFound
            
        
        
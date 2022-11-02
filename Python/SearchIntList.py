class Solution:
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
    """
    
    class Solution:
        def searchInsert(self, nums: list[int], target: int) -> int:
            """Doesn't work properly.

            Args:
                nums (list[int]): _description_
                target (int): _description_

            Returns:
                int: _description_
            """
            highIndex = len(nums) - 1
            lowIndex = 0
            
            print("input = ", nums)
            print("target = ", target)
            
            #while both search indices haven't converged or passed one another
            while( lowIndex != highIndex and lowIndex <= highIndex):
                #find new middle index
                midIndex = int( (highIndex + lowIndex) / 2 )
                
                #mid index #
                midNum = nums[midIndex]
                
                print("new mid index = ", midIndex)
                print("high index = ", highIndex)
                print("low index = ", lowIndex)
                
                #if point tween high+low is target
                if( midNum == target ):
                    return midIndex
                #if mid higher than target
                elif( midNum > target ):
                    if(highIndex == midIndex):
                        #if(midNumber == nums[highIndex]):
                        #    return highIndex
                        break
                    #assign new high index one spot below non-target mid
                    highIndex = midIndex
                #if mid lower than target
                else:
                    if(lowIndex == midIndex):
                        #if(midNum == nums[lowIndex]):
                        #    return lowIndex
                        break
                    #assign new bot index right above non-target mid
                    lowIndex = midIndex
            
            #target isn't in the list
            print("Target isn't in the list") 
            
            print("high index = ", highIndex)
            print("low index = ", lowIndex)
            
            #if lwo and high index the same as target
            if(nums[lowIndex] == target and nums[highIndex] == target ):
                #return either index
                return highIndex
            #if target less than low index + greater than high index
            elif(nums[lowIndex] > target and target > nums[highIndex]):
                return lowIndex
            #if target greater than low index + less than high index
            elif(nums[lowIndex] < target and target < nums[highIndex]):
                return highIndex 
            #if target less than both
            elif(nums[lowIndex] > target and nums[highIndex] > target):
                return 0
            elif(nums[lowIndex] < target and nums[highIndex] < target):
                return highIndex+1
            
    def stolenSearchInsert(self, nums: list[int], target: int) -> int:
        """Taken off online and not sure why works so well. Likely bc it converged in the lower index and not the upper.

            Binary search for target
                if not found, index to the right of last middle ret'd, which should be insert loc

        Args:
            nums (list[int]): _description_
            target (int): _description_

        Returns:
            int: _description_
        """
        l,r = 0, len(nums)
        #while left is bigger than right
        while l < r:
            #calc middle
            m = (l+r) // 2
            #if middle is target
            if nums[m] == target:
                return m
            #if middle less than target
            if nums[m] < target:
                #set left above middle
                l = m + 1
            #if middle more than target
            else:
                #set right at middle
                r = m
        #return left
        return l
print( Solution.searchInsert(self=Solution, nums=[1,3,5,6], target=2) )
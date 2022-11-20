class Solution:
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    """
    def runningSum(self, nums: list[int]) -> list[int]:
        """caches previous number of new arr in temp var so access arr less often

        Args:
            nums (list[int]): _description_

        Returns:
            list[int]: _description_
        """
        
        newArr = []
        
        for i,num in enumerate(nums):
            if i == 0:
                newArr.append(num)
                prevNum = num
            else:
                newNum = num+prevNum
                newArr.append(newNum)
                prevNum = newNum
            
        return newArr
    
sol = Solution()

print(sol.runningSum([1,2,3]) )
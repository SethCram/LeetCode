class Solution:
    def twoSum_my(self, nums: list[int], target: int) -> list[int]:
        """
            Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

            You may assume that each input would have exactly one solution, and you may not use the same element twice.

            You can return the answer in any order.
            
            Speed: O(N^N)
            Space: O(1)
        """
        
        iterations = 0
        
        for i in range(len(nums)):
            iVal = nums[i]
            
            for j in range(len(nums)):
                
                iterations += 1
                
                if i != j:
                    sum = iVal + nums[j]
                    
                    if sum == target:
                        
                        print(f"Iterations reqd = {iterations}")
                        
                        return [i, j]
                
    
    def twoSum_sol(self, nums: list[int], target: int) -> list[int]:
        """
            Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

            You may assume that each input would have exactly one solution, and you may not use the same element twice.

            You can return the answer in any order.
            
            Speed: O(N)
            Space: O(N)
        """
        
        history = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            
            reqdDiff = target - num
            
            #if desired diff to get to target has previously been seen
            if reqdDiff in history:
                #ret index of prev num and curr num
                return [ history[reqdDiff], i]
            
            #if desired diff hasn't been seen yet
            else:
                #store num along with its index
                history[ num ] = i
                            
                
nums = [1,2,3,4,5,6,7]

rslt = Solution.twoSum_sol(self=Solution, nums=nums, target=3)

print(rslt)
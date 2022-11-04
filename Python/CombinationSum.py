class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Instructions:
            Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

            The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

            The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

        DFS solution
        
        Args:
            candidates (list[int]): _description_
            target (int): _description_

        Returns:
            list[list[int]]: _description_
        """
        
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        #can't have negative target?
        if target < 0:
            return 
        
        if target == 0:
            ret.append(path)
            return 
        
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path + [nums[i]], ret)

sol = Solution()

print( sol.combinationSum(candidates=[2,3,6,7], target=7) )            

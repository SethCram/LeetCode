class Solution:
    """
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.
    """
    def pivotIndex_Slow(self, nums: list[int]) -> int:
        """
        Speed: O(N^N) bc walks thru the arr once every move right
        Space: O(1)

        Args:
            nums (list[int]): _description_

        Returns:
            int: _description_
        """
        
        numsLen = len(nums)
        
        for i,num in enumerate(nums):
            if i == 0:
                lhsSum = 0
            else:
                lhsSum = sum(nums[:i])
            if i == numsLen - 1:
                rhsSum = 0
            else:
                rhsSum = sum(nums[i+1:])
            
            if rhsSum == lhsSum:
                return i
        
        return -1
    
    def pivotIndex_Fast(self, nums: list[int]) -> int:
        """
        Speed: O(2N) bc half to walk thru arr twice, once to init rhsSum, once as iterating
            (technically O(N) since consts dont matter)
        Space: O(1)

        Args:
            nums (list[int]): _description_

        Returns:
            int: _description_
        """
        for i,num in enumerate(nums):
            if i == 0:
                #init both sums
                lhsSum = 0
                rhsSum = sum(nums[i+1:])
            else:
                #update lhs sum
                lhsSum = lhsSum + nums[i-1]
                #update rhs sum
                rhsSum = rhsSum - num
            
            if rhsSum == lhsSum:
                return i
        
        return -1
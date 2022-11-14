class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Speed: O( (N+M)log(N+M) ) bc that's the speed of the Timsort algorithm python's builtin sort() uses
        Space: O( N+M )

        Args:
            nums1 (list[int]): _description_
            nums2 (list[int]): _description_

        Returns:
            float: _description_
        """
        
        comboNums = nums1 + nums2
        
        comboNums.sort()
        
        comboNumsLen = len(comboNums)
        
        middleIndex = comboNumsLen / 2
        
        if comboNumsLen % 2 == 0:
            return (comboNums[int(middleIndex-0.5)] + comboNums[int(middleIndex+0.5)]) / 2
        else:
            return comboNums[int(middleIndex)]
        
sol = Solution()

print( sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]) )
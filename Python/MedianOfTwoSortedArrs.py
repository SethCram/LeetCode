import sys


class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays_BuiltinSort(self, nums1: list[int], nums2: list[int]) -> float:
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
        
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Speed: O( log( min(x,y) ) )
        Space: O( N+M )
        
        Find partition through doing a binary search on the small list 
            and find such a point that every every element on the left 
            side of both lists is less than every element on the right side.
        Then, median = avg( max(rightmost_nums1_sublist, rightmost_nums2_sublist) )

        Args:
            nums1 (list[int]): _description_
            nums2 (list[int]): _description_

        Returns:
            float: _description_
        """
        
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2: return self.findMedianSortedArrays(nums2, nums1)
        nums1 += [float('inf'), float('-inf')]
        nums2 += [float('inf'), float('-inf')]
        left, right = 0, 2 * n2
        while left <= right:
            mid2 = left + (right - left) // 2
            mid1 = n1 + n2 - mid2
            L1, R1 = nums1[(mid1-1) // 2], nums1[mid1 // 2]
            L2, R2 = nums2[(mid2-1) // 2], nums2[mid2 // 2]
            if L1 > R2:
                left = mid2 + 1
            elif L2 > R1:
                right = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2
        
sol = Solution()

print( sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]) )
from math import ceil

class Solution:
  """
  Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

  You must write an algorithm with O(log n) runtime complexity.
  """
  def search_arrslicing(self, nums: list[int], target: int) -> int:
      """Non recursive 'interval'/binary search. Requires data set in ascending order.
      Uses arr slicing

      Args:
          nums (list[int]): Requires data set in ascending order.
          target (int): Nubmer looking for

      Returns:
          int: _description_
      """
      finalIndex = 0
      while( len(nums) > 0 ):
          
          #print("New nums = ", nums)
          
          numsLength = len(nums)
          halfwayIndex = int( numsLength/2 )
          halfwayInt = nums[halfwayIndex]

          if( halfwayInt == target ):
              #incr to final index
              finalIndex += halfwayIndex
          
              return finalIndex
          elif( numsLength == 1):
            break
          
          elif( halfwayInt > target ):
          
              if(numsLength == 2):
                if( target == nums[0] ):
                  return finalIndex
                else:
                  break
              else:
                  #take lower half inclusive
                  nums = nums[0:halfwayIndex]
              
          elif( halfwayInt < target ):
          
              #take upper half inclusive
              
              if(numsLength == 2):
                  if( target == nums[numsLength-1] ):
                    return finalIndex
                  else:
                    break
              else:
                  #account for cutting out half of numbers
                  finalIndex += halfwayIndex
                  
                  nums = nums[halfwayIndex:numsLength]
      return -1
        
  def search_doubleptr(self, nums: list[int], target: int) -> int:
      """Double ptr approach. 
        Could possibly use round() instead of ciel(), but even rounding instead of upper bound.
        Requires data structure with constant access time like arr.
      
      Time Complexity: O(logN)
      Space: O(1)

      Args:
          nums (list[int]): _description_
          target (int): _description_

      Returns:
          int: _description_
      """
        
      #print(f"{nums}, {target}")
      
      leftPtr = 0
      rightPtr = len(nums) - 1
      
      while leftPtr <= rightPtr: #must check equal case since both left and right ptrs move to unchecked nums
          
          middleIndex = ceil((rightPtr + leftPtr)/2) #consistent rounding up instead of to nearest even num (round())
          middleNum = nums[middleIndex]
          
          if middleNum == target:
              #print(middleIndex)
              return middleIndex
          elif middleNum < target:
              leftPtr = middleIndex + 1 #need to add 1 so doesn't inf loop at adjacent nums case
          elif middleNum > target:
              rightPtr = middleIndex - 1 #need to subtr 1 so doesn't inf loop at adjacent nums case
      
          #print(f"{leftPtr}, {rightPtr}")
      
      return -1
      
print( Solution.search(self=Solution, nums=[-1,0,3,5,9,12], target=9) )
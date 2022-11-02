class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Non recursive 'interval'/binary search. Requires data set in ascending order.

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
          
print( Solution.search(self=Solution, nums=[-1,0,3,5,9,12], target=9) )
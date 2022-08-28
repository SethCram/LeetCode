class Solution:
   
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
        
    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
    
    Your solution must use only constant extra space. ??
    You may not use the same element twice. ??
    
    The tests are generated such that there is exactly one solution. (no input lists w/ mult sets of nums that can add up to target val)
    """
    def timeOutTwoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Brute force approach. Attempted optimization but it still times out.
        """
        
        operand1Index = 0
        operand2Index = 1
        
        sumReached = False
        
        #cache count 
        numbersCount = len( numbers )
        
        for num1 in numbers:
            
            #loop thru numbers indexed 1 to count-1
            while(operand2Index < numbersCount):
                
                num2 = numbers[operand2Index]
                
                #if added numbers get us target
                if( num1 + num2 == target):
                    #we're at the right indices so break out
                    sumReached = True
                    break
                
                #if num1 positive + num2 greater than target, or sum is greater than target
                if( (num1 >= 0 and num2 > target) or num1 + num2 > target ):
                    #break bc ready to start on nxt num1
                    break
                    
                operand2Index += 1
            
            #if we reached our sum
            if(sumReached):
                #break so dont incr index or rst index
                break
            
            #advance index
            operand1Index += 1
            
            #make sure index2 is reset properly to right in front of new index1
            operand2Index = operand1Index+1
                
        operand1Index += 1
        operand2Index += 1
        
        return ( operand1Index, operand2Index )
        
        

nums = [1,2,3,4,4,9,56,90]

newList = Solution.twoSum(self=Solution, numbers=nums, target= 8)

print(newList)
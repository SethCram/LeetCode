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
        
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Approach: Divide and conquer using a binary search. 
            Keep num1 same and repeatedly choose num2 as the new middle till a number is converged upon by the search indices. 
            If don't find sum, incr num1 index and repeat process to find a matching num2 for sum.

        Better approach would be to progressively move the LHS and RHS indices closer to one another until a sol is found.
            (since og list sorted non-decr order) (would only see each val once)

        Args:
            numbers (List[int]): _description_
            target (int): _description_

        Returns:
            List[int]: _description_
        """
        #cache count 
        numbersCount = len( numbers )
        
        highIndex = numbersCount-1
        lowIndex = 1
        
        operand1Index = 0 #not same as low index
        operand2Index = (lowIndex + highIndex) // 2 #double // for int
        
        #while haven't reached count w/ operand1Index
        while( operand1Index < numbersCount):
            
            num1 = numbers[operand1Index]
            num2 = numbers[operand2Index]
            
            numSum = num1 + num2
            
            if( numSum  == target):
                break
            #if search indices converged
            elif( lowIndex == highIndex ):
                #advance index1 bc need greater num1
                operand1Index += 1
                
                #reset high + low indices for new triangulating
                lowIndex = operand1Index + 1
                highIndex = numbersCount - 1
                
            #if sum less than target
            elif( numSum < target ):
                
                #need greater num2 so high lowIndex
                lowIndex = operand2Index + 1
                
            #if sum more than target
            elif (numSum > target):
                #prevSumGTTarget = True
                
                #need lesser num2 so lower highIndex
                highIndex = operand2Index
                
            #make sure index2 is reset properly to mid
            operand2Index = (lowIndex + highIndex) // 2
        
        
        operand1Index += 1
        operand2Index += 1
        
        return ( operand1Index, operand2Index )

    # two-pointer
    # speed: O(N)
    # space: O(1) = constant
    def twoSumPointers(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

nums = [1,3,4,4]

newList = Solution.twoSum(self=Solution, numbers=nums, target= 8)

print(newList)
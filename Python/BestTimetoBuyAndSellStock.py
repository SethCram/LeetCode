class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Double pointer approach with constant storage
        Time Complexity: O(N)
        Space: O(1)

        Args:
            prices (list[int]): _description_

        Returns:
            int: _description_
        """
        for i,price in enumerate(prices):
            
            #init pointers and diff
            if i == 0:
                smallest = price
                largest = 0
                largestDifference = largest - smallest
            #set new largest/smallest as seen and track largest diff
            else:
                #if new largest
                if price > largest:
                    largest = price
                    
                #if new smallest
                if price < smallest:
                    #if curr diff larger than largest diff
                    currDifference = largest - smallest
                    if currDifference > largestDifference:
                        #overwrite largest as curr diff
                        largestDifference = currDifference
                    
                    #set new smallest and look for new largest
                    smallest = price
                    largest = 0
            
            #print(f"{largest}, {smallest}")
        
        currDifference = largest - smallest
        
        #return largest diff or 0
        if largestDifference > currDifference:
            return largestDifference
        elif largest <= smallest:
            return 0
        else:
            return largest - smallest
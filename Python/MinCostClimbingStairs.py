import math


class Solution:
    def minCostClimbingStairs_Slow(self, cost: List[int]) -> int:
        """Tree approach using recursion. Times out bc iterates over already seen vals multiple times.
        v + E >> N
        Speed: O(2^N)?

        Args:
            cost (List[int]): _description_

        Returns:
            int: _description_
        """
        
        #inits minCost higher than any route cost could ever be (due to constraints)
        
        return min(
                self.findMinCost_Recursive(cost, 0, 999_999, 0), 
                self.findMinCost_Recursive(cost, 1, 999_999, 0)
            )
        
    def findMinCost_Recursive(self, cost, rootIndex, minCost, pathCost) -> int:
        
        costListLen = len(cost)
        
        if rootIndex >= costListLen:
            return pathCost
        
        pathCost += cost[rootIndex]
        
        #print(pathCost)
        
        minestPath = min(
                self.findMinCost_Recursive(cost, rootIndex+1, minCost, pathCost), 
                self.findMinCost_Recursive(cost, rootIndex+2, minCost, pathCost)
            ) 
           
        #print(minCostPathOne)
        #print(minCostPathTwo)
            
        if minestPath < minCost:
            minCost = minestPath
        
        return minCost
    
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """Iteration with temporary vars to keep track of 2 possible paths.
        Speed: O(N)
        Space: O(1)

        Args:
            cost (list[int]): _description_

        Returns:
            int: _description_
        """
        #init diff path vals
        firstNum = cost[0]
        secondNum = cost[1]
        
        #catch
        if len(cost) <= 2:
            return min(firstNum, secondNum)
        
        #walk thru rest of cost ellies after first 2
        for costElly in cost[2:]:
            #accumulate smallest cost path from a previous start
            currNum = costElly + min(firstNum, secondNum)
            #save two spaces ahead for nxt go
            firstNum = secondNum
            #save curr sum for nxt go
            secondNum = currNum
            
        return min(firstNum, secondNum)
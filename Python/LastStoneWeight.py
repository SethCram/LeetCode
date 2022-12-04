import heapq
from copy import deepcopy

class Solution:
    """
    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left, return 0.
    """
    def lastStoneWeight(self, stones: list[int]) -> int:
        """Priority queue implemented through a max heap.
        Speed: O(NlogN) bc inserting a new key takes O(Logn) (at most once per number), 
            popping key also takes O(Logn) time (at most twice per number, but numbers get added too), 
            and creating initial heap requires a full pass through list
            
            Worst case speed is likely O((3*N)*(3*logN)) but constants don't mater long term

        Args:
            stones (list[int]): _description_

        Returns:
            int: _description_
        """
        #copy list so isn't clobbered
        maxHeap = deepcopy([-stone for stone in stones])
        
        #create min-heap using negative of vals (so actually max heap)
        heapq.heapify(maxHeap) #op done in-place
        
        while True:
            
            print(maxHeap)
            
            if len(maxHeap) == 0:
                return 0
            
            bigger = -1*heapq.heappop(maxHeap)
            
            if len(maxHeap) == 0:
                return bigger
            
            smaller = -1*heapq.heappop(maxHeap)
            
            #if nums unequal, add difference back into heap
            if bigger != smaller:
                heapq.heappush(maxHeap, smaller-bigger) #push negative equivalent of difference
                
        
        
from math import ceil
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [head]
        numOfNodes = 1
        
        nxtNode = head

        #while not at end of list
        while(nxtNode.next != None):
            #go to next elly
            nxtNode = nxtNode.next
            
            #append next node to list of nodes
            nodes.append( nxtNode )
            
            #incr elly count
            numOfNodes += 1
            
        removalIndex = numOfNodes - 1 - n
            
        #if more than 1 node and not removing last node
        if(numOfNodes > 1  and n != 0):
            #link prev node's nxt to removal node's next
            nodes[removalIndex-1].next = nodes[removalIndex].next
        #only one node in list
        elif( numOfNodes == 1 ):
            nodes[removalIndex] = None
        
        return nodes[0]
    
middleNode = Solution.middleNode(Solution, [1,2,3,4,5])

print(middleNode)
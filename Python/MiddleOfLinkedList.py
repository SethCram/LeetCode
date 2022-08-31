from math import ceil
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
            
        #print(numOfNodes)
        #print(ceil(numOfNodes / 2)-1)
        #print(nodes[ceil(numOfNodes / 2)-1])

        #if even number of nodes
        if( numOfNodes % 2 == 0 ):
            return nodes[ceil(numOfNodes / 2)]
        #if odd num of nodes
        else:
            return nodes[ceil(numOfNodes / 2)-1]
    
middleNode = Solution.middleNode(Solution, [1,2,3,4,5])

print(middleNode)
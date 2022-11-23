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

Speed: O(N)
Space: O(N)
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Speed: O(N)
        Space: O(N)

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
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
    
    def MiddleNodeSol(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Double pointer approach.
            slower pntr goes 1 by 1, fast pntr 2 by 2.
            when fast pntr reaches the end, slower pntr will be at the middle of the list.
        Speed: O(N)
        Space: O(1)

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
middleNode = Solution.middleNode(Solution, [1,2,3,4,5])

print(middleNode)
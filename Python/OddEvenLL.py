# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from pyparsing import Optional


class Solution:
    """
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Double pointer approach
        Speed: O(N) bc only iterate thru LL once,
            but last reconnecting of node overwritten if ended on an even node
        Space: O(1) bc only cache 1 node

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """

        #if LL 0, 1, or 2 nodes in it
        if head == None or head.next == None or head.next.next == None:
            #dont need to change LL at all
            return head

        ogHead = head
        currNode = head
        prevNode = head
        nodeCount = 1

        #walk LL till at the last node
        while(currNode.next != None):
            
            #connect connection to every other connection
            prevNode = currNode
            
            currNode = currNode.next
            nodeCount += 1
            #if first even node, cache it
            if(nodeCount == 2):
                firstEvenNode = currNode

            prevNode.next = currNode.next
        
        #if last node is odd
        if(nodeCount % 2 != 0): #previously odd
            #connect last odd node to start of even LL
            currNode.next = firstEvenNode
        #if last node is even
        else:
            #connect last odd node to start of even LL
            prevNode.next = firstEvenNode

        return ogHead
        
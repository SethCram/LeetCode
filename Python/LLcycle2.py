from pyparsing import Optional
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    """
    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.
    """
    def detectCycle_slow(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Sound solution but times out
        Speed: O(N^N)
        Space: O(N) but could iterate thru prev seen nodes using indexing instead

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        prevNodes = []
        
        #headIndex = 0
        
        #walk thru LL
        while(head != None):
            #add to prev node list
            prevNodes.append(head)
            #walk thru prevNodes
            for prevNode in prevNodes:
                #if next head node is a prevNode
                if head.next is prevNode:
                    #return the prev node's index
                    return prevNode
            
            #advance head
            head = head.next
            #headIndex += 1
        
        return None


    def detectCycle_fast(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Uses a dictionary for hashing and accessing vals quickly
        Speed: O(N)
        Space: O(N)

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        #init prevNodes dict with the head node
        prevNodes = defaultdict(bool) #could also be a lambda expresh or funct
        prevNodes[head] = True
        
        #walk thru LL
        while(head != None):
            #if next node already seen before
            if prevNodes[head.next] == True:
                #return it
                return head.next
            #if next node not seen before, mark it as seen before
            else:
                prevNodes[head.next] = True
            
            #advance head
            head = head.next
        
        return None

    def detectCycle_sol(self, head):
        """Double pointer approach (don't understand)
        Speed: O(N)
        Space: O(1)

        Args:
            head (_type_): _description_

        Returns:
            _type_: _description_
        """
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
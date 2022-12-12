# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    """
    Given the head of a linked list, return the list after sorting it in ascending order.
    """    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LL merge sort using tortoise and hare alg to find middle nodes.
        Speed: O(NlogN) bc use merge sort,
            (iterations used for tortoise + hare alg not taken into act?)
        Space: O(logN), mainly due to recursion funct stack frame,
            (should be O(NlogN) since we create a new node for ever additional LL w/ merging?)
            Can use constant space if use bottom-up iterative solution instead of top-down

        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        #if LL of size 0 or 1, broken into most basic building blocks (base case)
        if(head == None or head.next == None):
            return head
        
        fast = head
        slow = head
        slower = None
        
        #find list middle for start of 2nd list of before it for start of 2nd
        while(fast != None and fast.next != None):
            slower = slow
            slow = slow.next
            fast = fast.next.next
        slower.next = None

        #print(f"Split into {head} and {slow}")
        
        #start of 1st half LL
        list1head = self.sortList(head)
        #start of 2nd half LL
        list2head = self.sortList(slow)

        #print(head.val)

        #after breaking down both halves of LL, merge them
        return self.mergeList(list1head, list2head)
    
    def mergeList(self, list1head, list2head):
        
        newLL = ListNode()
        
        beforeNewHead = newLL
        
        #walk thru LLs
        while(list1head != None and list2head != None):
            
            #Add smaller val to newLL
            if(list1head.val < list2head.val):
                newLL.next = list1head
                list1head = list1head.next
            else:
                newLL.next = list2head
                list2head = list2head.next

            #advance newLL head to add more nodes 
            newLL = newLL.next
        
        #if LLs not both reached end, attach rest of LL onto its end
        if(list1head != None):
            newLL.next = list1head
        
        if(list2head != None):
            newLL.next = list2head

        #print(f"Merged to {beforeNewHead.next}")
        
        #ret new LL head
        return beforeNewHead.next
        
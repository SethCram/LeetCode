from pyparsing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Double pointer approach 
        Speed: O(N+M) where N = nodes in list1, M = nodes in list2
        Auxillary Space: O(1)
        Space: O(N+M)

        Args:
            list1 (Optional[ListNode]): _description_
            list2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        #if 1 list isnt none
        if list1 != None or list2 != None:
            comboLL = ListNode()
            newListHead = comboLL
        #if both lists are none
        else:
            return None
        
        #while both lists not yet gone thru
        while list1 != None or list2 != None:
            
            #advance list not yet reaching its end
            if list1 == None:
                nxtNode = list2
                list2 = list2.next
            #advance list not yet reaching its end
            elif list2 == None:
                nxtNode = list1
                list1 = list1.next
            #advance list w/ smaller val
            else:
                if list1.val < list2.val:
                    nxtNode = list1
                    list1 = list1.next
                else:
                    nxtNode = list2
                    list2 = list2.next
            
            #set comboLL val
            comboLL.val = nxtNode.val
            
            #if either list not done yet
            if list1 != None or list2 != None:
                #create new node for combo LL
                comboLL.next = ListNode()
                #advance comboLL to next node
                comboLL = comboLL.next 
            
        return newListHead
            
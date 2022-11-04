import copy


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
     def __str__(self) -> str:
         newList = []
         
         while self != None:
             newList.append(self.val)
             self = self.next
            
         return str(newList)

class Solution:
    def ReverseLL(self, head):
        """Triple pointer approach. Head node doesn't change.
        Speed: O(N)
        Space: O(1)
        """
        
        #prevents original list from being clobbered
        head = copy.deepcopy(head)
        
        #init pointers
        prevNode = head
        prevPrevNode = None
        
        while head != None:
            #advance head
            head = head.next
            
            #reverse link
            prevNode.next = prevPrevNode
            
            #advance pointers
            prevPrevNode = prevNode
            prevNode = head
          
        #print(head)
        head = prevPrevNode #shouldn't this set head correctly?? Seems to but l1 remains at 2
        print(f"Head During: {head}")
        
        return head
            
sol = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = None

print(f"Head Before: {l1}")
print(f"Function Returns: {sol.ReverseLL(l1)}" )
print(f"Head After: {l1}")
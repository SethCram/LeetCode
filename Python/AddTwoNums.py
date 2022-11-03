# Definition for singly-linked list.
from typing import Optional


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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Accounts for differnt size LLs through checking for None and using ph vals.
        Uses a carryOver to account for single digit addition overflow.
        speed: O(N)
        auxiliarry space: O(1)

        Args:
            l1 (Optional[ListNode]): _description_
            l2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        
        #init head
        l3 = ListNode()
        head = l3
        
        carryOver = 0
        
        #while either list still not finished
        while l1 != None or l2 != None:
            
            if l1 == None:
                l1Val = 0
                l1Next = None
            else:
                l1Val = l1.val
                l1Next = l1.next
            
            if l2 == None:
                l2Val = 0
                l2Next = None
            else:
                l2Val = l2.val
                l2Next = l2.next
        
            phSum = l1Val + l2Val + int(carryOver)
            
            phSumStr = str(phSum)
            
            digitsInSum = len(phSumStr)
            
            if digitsInSum > 1:
                carryOver = phSumStr[0:digitsInSum-1]
            else:
                carryOver = 0
                
            l3.val = int(phSumStr[-1])
            
            #if haven't reached end of lists
            if l1Next != None or l2Next != None:
                l3.next = ListNode()
            #if still carry over and reached end of both lists
            elif carryOver != 0:
                #create new node and advance to it
                l3.next = ListNode()
                l3 = l3.next
                #put carryOver here
                l3.val = carryOver
                #terminate l3
                l3.next = None
                
            #if no carry over and reached end of lists
            else:
                #terminate l3
                l3.next = None
            
            #advance every list node pointer if not at end of respective list
            l3 = l3.next
            
            if l2 != None:
                l2 = l2.next
            
            if l1 != None:
                l1 = l1.next
                
        #print(l3)
        
        return head
    
sol = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = None
#l2 = [5,6,4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = None
print(sol.addTwoNumbers(l1, l2))
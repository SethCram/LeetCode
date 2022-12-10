
 //Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}

/// <summary>
/// Given the head of a linked list, remove the nth node from the end of the list and return its head
/// </summary>
public class Solution {
    /// <summary>
    /// Time Complexity: O(N) bc only 1 pass thru LL
    /// Space Complexity: O(N) bc entire LL copied into list for indexing
    /// </summary>
    /// <param name="head"></param>
    /// <param name="n"></param>
    /// <returns></returns>
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        
        List<ListNode> seenNodes = new List<ListNode>();

        ListNode ogHead = head;

        int lengthCounter = 0;

        //walk thru LL + add nodes to new list + count its length
        while(head != null)
        {
            //add seen node
            seenNodes.Add(head);

            //advance node + counter
            head = head.next;
            lengthCounter++;
        }

        int removeIndex = lengthCounter - n;

        //Console.WriteLine($"{removeIndex.ToString()}, {lengthCounter.ToString()}");

        //if removing head + more than 1 node
        if(removeIndex == 0 && lengthCounter > 1)
        {
            //set head to next node
            ogHead = seenNodes[1];
        }
        //if removing head + only 1 node
        else if(removeIndex == 0)
        {
            //clear head
            ogHead = null;
        }
        //if removing anything besides head
        else
        {
            //set prev node's next as removal node's next
            seenNodes[removeIndex - 1].next = seenNodes[removeIndex].next;
        }

        return ogHead;
    }
}
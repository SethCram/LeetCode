
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
public class RemoveNthNodeFromEndofList {
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

public class RemoveNthNodeFromEndofList2 {
    /// <summary> 
    /// Double pointer approach maintaining n+1 distance tween them
    /// Speed: O(N)
    /// Space: O(1)
    /// </summary>
    /// <param name="head"></param>
    /// <param name="n"></param>
    /// <returns></returns>
    public ListNode RemoveNthFromEnd(ListNode head, int n) {

        ListNode ogHead = head;

        ListNode beforeRemovalNode = head;

        int lengthCounter = 0;

        int beforeRemovalIndex = 0;

        //walk thru LL + add nodes to new list + count its length
        while(head != null)
        {
            //advance node + counter
            head = head.next;
            lengthCounter++;

            //if two pntrs too far apart, advance removal node
            if((lengthCounter - beforeRemovalIndex) > n+1) //wanna be right before removal node
            {
                beforeRemovalNode = beforeRemovalNode.next;
            }
        }

        //Console.WriteLine($"{removeIndex.ToString()}, {lengthCounter.ToString()}");

        int removalIndex = lengthCounter - n;

        //if removing head + more than 1 node
        if(removalIndex == 0 && lengthCounter > 1)
        {
            //set head to next node
            ogHead = beforeRemovalNode.next;
        }
        //if removing head + only 1 node
        else if(removalIndex == 0)
        {
            //clear head
            ogHead = null;
        }
        //if removing anything besides head
        else
        {
            //set prev node's next as removal node's next
            beforeRemovalNode.next = beforeRemovalNode.next.next;
        }

        return ogHead;
    }
}
#include<iostream>

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

/// @brief Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
class Solution {
public:
    /// @brief Leverages Floyd's/Tortoise and Hair alg, and list reversal
    /// @brief Speed: O(N) bc only iterate for as many nodes as there are (doesn't matter how many times see each)
    /// @brief Space: O(1)
    /// @param head 
    /// @return 
    bool isPalindrome(ListNode* head) {
        
        ListNode* prevPrevSlow = nullptr;
        ListNode* prevSlow = nullptr;
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* reversePntr = head;

        while (fast != nullptr && fast->next != nullptr) //always use '->' to access pointer props
        {

            //printf("%d %d", fast->val, fast->next->next->val);

            //advance reverse LL pntrs
            prevPrevSlow = prevSlow;
            prevSlow = slow;

            //floyd's alg to find center
            slow = slow->next;
            fast = fast->next->next;

            //reverse connection
            prevSlow->next = prevPrevSlow;
        }

        //if odd number of nodes bc ended on a node (not null)
        if(fast != nullptr)
        {
            //make sure slow pntr doesn't start in middle
            slow = slow->next;
        }

        while(slow != nullptr)
        {
            if(prevSlow->val != slow->val)
            {
                return false;
            }

            //advance pntrs in opposite dir
            prevSlow = prevSlow->next;
            slow = slow->next;
        }

        return true;
    }
};
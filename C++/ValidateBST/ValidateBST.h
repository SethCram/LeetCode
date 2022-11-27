#include <stdio.h>


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/// @brief Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.
class Solution1 {
public:
    /// @brief 
    /// @param root 
    /// @return 
    bool isValidBST(TreeNode* root) {
        
        if(root == nullptr) // C++ has alota diff nulls
        {
            return true;
        }
        
        int rootVal = root -> val;
        
        printf("Root val %d\n", rootVal);
        
        TreeNode* leftNode = root -> left;
        TreeNode* rightNode = root -> right;
        
        bool functResponse = true;
        
        if(leftNode != nullptr)
        {
            if(leftNode -> val < rootVal)
            {
                //only propogate response if negative
                if( !isValidBST(leftNode) )
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        
        if(rightNode != nullptr)
        {
            if(rightNode -> val > rootVal)
            {
                //only propogate response if negative
                if( !isValidBST(rightNode) )
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        
        return true; //why is this needed?
        
    }
};

#include <stdio.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution2 {
public:
    bool isValidBST(TreeNode* root) {
        
        return isValidBST_Recursion(root, nullptr);
        
    }
    
private:
    bool isValidBST_Recursion(TreeNode* root, TreeNode* parent, bool rightTree = false)
    {
        if(root == nullptr) // C++ has alota diff nulls
        {
            return true;
        }
        
        int rootVal = root -> val;
        
        printf("Root val %d\n", rootVal);
        
        TreeNode* leftNode = root -> left;
        TreeNode* rightNode = root -> right;
        
        bool functResponse = true;
        
        if(leftNode != nullptr)
        {
            int leftNodeVal = leftNode -> val;
            
            if(leftNodeVal < rootVal)
            {
                if(parent != nullptr)
                {
                    int parentNodeVal = parent -> val;
                    
                    //if right tree of parent
                    if(rightTree)
                    {
                        if( parentNodeVal > leftNodeVal )
                        {
                            return false;
                        }
                    }
                }
                
                //only propogate response if negative
                if( !isValidBST_Recursion(leftNode, root, false) )
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        
        if(rightNode != nullptr)
        {
            int rightNodeVal = rightNode -> val;
            
            if(rightNodeVal > rootVal)
            {
                if(parent != nullptr)
                {
                    int parentNodeVal = parent -> val;
                    
                    //if left tree of parent
                    if(!rightTree)
                    {
                        if( parentNodeVal < rightNodeVal )
                        {
                            return false;
                        }
                    }
                }
                
                //only propogate response if negative
                if( !isValidBST_Recursion(rightNode, root, true) )
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        
        return true; //why is this needed?
    }
};
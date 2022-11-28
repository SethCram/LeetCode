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
class Solution3 {
public:
    bool isValidBST(TreeNode* root) {
        
        return isValidBST_Recursion(root, root -> val, root -> val); //always atleast the root
        
    }
    
private:
    bool isValidBST_Recursion(TreeNode* root, int minValFound, int maxValFound)
    {
        if(root == nullptr) // C++ has alota diff nulls
        {
            return true;
        }
        
        int rootVal = root -> val;
        
        if(rootVal < minValFound)
        {
            minValFound = rootVal;
        }
        
        if(rootVal > maxValFound)
        {
            maxValFound = rootVal;
        }
        
        printf("Root val %d, min %d, max %d\n", rootVal, minValFound, maxValFound);
        
        TreeNode* leftNode = root -> left;
        TreeNode* rightNode = root -> right;
        
        if(leftNode != nullptr)
        {
            int leftNodeVal = leftNode -> val;
            
            //if a left node is ever bigger than another node
            if( minValFound <= leftNodeVal )
            {
                return false;
            }

            //only propogate response if negative
            if( !isValidBST_Recursion(leftNode, minValFound, maxValFound) )
            {
                return false;
            }
        }
        
        if(rightNode != nullptr)
        {
            int rightNodeVal = rightNode -> val;
            
            //if another node is ever bigger than a right node
            if( maxValFound >= rightNodeVal )
            {
                return false;
            }

            //only propogate response if negative
            if( !isValidBST_Recursion(rightNode, minValFound, maxValFound) )
            {
                return false;
            }
        }
        
        return true; //why is this needed?
    }
};

class Solution_real {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* prev = NULL;
        return validate(root, prev);
    }
    bool validate(TreeNode* node, TreeNode* &prev) {
        //base case
        if (node == NULL) return true;
        //go down left subtree and propogate false if ret'd
        if (!validate(node->left, prev)) return false;
        //inorder traversal and checking 
        if (prev != NULL && prev->val >= node->val) return false;
        
        //printf("%d\n", node -> val);
        
        //specify (LHS child as prev node?), then shared parent node
        prev = node;
        //go down right subtree (doesn't propogate flase if ret'd?)
        return validate(node->right, prev);
    }
};
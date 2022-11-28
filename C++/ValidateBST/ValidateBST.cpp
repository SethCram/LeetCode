#include "ValidateBST.h"

int main()
{
    Solution_real solution = Solution_real();

    //TreeNode *c1 = &TreeNode(2);
    //TreeNode *c2 = &TreeNode(3);

    solution.isValidBST(
        &TreeNode(2, &TreeNode(2), &TreeNode(3))
    );
}
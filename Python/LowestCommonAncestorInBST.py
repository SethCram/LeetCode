#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.lowestCommonAncestor_Recursion(root, p, q, root)[2]
    
    def lowestCommonAncestor_Recursion(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', commonAncestor, foundP = False, foundQ = False, stop = False) -> tuple:
        
        #base case
        if root == None:
            return foundP, foundQ, commonAncestor, stop
        
        foundPleft, foundQleft, commonAncestorLeft, stopLeft = self.lowestCommonAncestor_Recursion(root.left, p, q, commonAncestor, foundP, foundQ, stop)
        
        foundPright, foundQright, commonAncestorRight, stopRight = self.lowestCommonAncestor_Recursion(root.right, p, q, commonAncestor, foundP, foundQ, stop)
        
        #postorder traversal 
            
        print(f"{root.val}, {foundP}, {foundQ}, {commonAncestor.val}")
        
        #if p found
        if root is p:
            print("p found")
            foundP = True
        #if q found
        elif root is q:
            print("q found")
            foundQ = True
        
        #if both p and q found for the first time 
        if foundP and foundQ:
            foundP = False
            foundQ = False
            
            return foundP, foundQ, root, True
        #propogate returning of LCA 
        else:
            return foundP, foundQ, commonAncestor, stop

class Solution_real:
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Leverages BST organization and recursion
        Speed: O(M) where M is the number of vertices and edges between the root node and the LCA
        Space: O(1)

        Args:
            root (TreeNode): _description_
            p (TreeNode): _description_
            q (TreeNode): _description_

        Returns:
            TreeNode: _description_
        """
        
        #base case unneeded since always guarateed root as LCA
        
        # how does this guarantee LOWEST common ancestor? bc it's a BST?
        
        #if curr node is too large, go down left subtree
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        #if curr node is too small, go down right subtree
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        #if made here, curr node is between val of p and q (or p or q), therefore an ancestor of them in a BST
        return root
    
sol = Solution()

startroot = TreeNode(-1)

root = startroot

for i in range(10):
    root.left = TreeNode(i)
    root.right = TreeNode(i*2)
    
    root = root.left

p = TreeNode(6)
q = TreeNode(9)

print(sol.lowestCommonAncestor(startroot, p, q).val)
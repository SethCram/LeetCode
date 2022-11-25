#from queue import Queue #use this one for multi proccing
from collections import deque

from pyparsing import Optional #use this one as data structure

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values. 
        (i.e., from left to right, level by level).
    """
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """BFS using a queue
        Speed: O(V+E) where V = number of vertices and E = number of edges
        Space: O(V^2) bc use a queue and list
        Auxilliary Space: O(V) bc only use a queue for intermediate steps

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            list[list[int]]: _description_
        """
        
        #empty list catch
        if root == None or root == []:
            return []
        
        q = deque() 
        
        q.append(root)
        
        outputList = [[root.val]]
        
        lvlLength = 1
        
        while len(q) > 0:

            lvlList = []
            
            #for every node found for this lvl
            for _ in range(lvlLength):
                #pop node off queue
                currNode = q.popleft()

                leftNode = currNode.left
                rightNode = currNode.right

                #add left and right nodes if not null
                if leftNode != None:
                    q.append(leftNode)
                    lvlList.append(leftNode.val)
                if rightNode != None:
                    q.append(rightNode)
                    lvlList.append(rightNode.val)
            
            #update lvl length for next lvl down
            lvlLength = len(lvlList)        
            
            #append this level 
            if lvlList != None and lvlList != []:
                outputList.append(lvlList)

        return outputList
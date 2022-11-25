# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    """
    Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
    """
    def preorder(self, root: Node) -> list[int]:
        """DFS using recursion
        Time Complexity: O(V+E) where V = number of vertexes, E = number of edges
        Space: O(V)
        Auxilliary Space: O(1)

        Args:
            root (Node): _description_

        Returns:
            list[int]: _description_
        """
        outputList = []
        
        #only use recursion if list of nodes
        if root != [] and root != None:
            self.preorder_recursion(root, outputList)
        
        return outputList
        
    def preorder_recursion(self, root: 'Node', outputList: list):
        
        outputList.append(root.val)
        
        #base case
        if root.children == None:
            return 
        
        for child in root.children:
            self.preorder_recursion(child, outputList)
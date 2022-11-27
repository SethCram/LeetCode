import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution
{

    public static void main (String[] args) 
    {
        System.out.println(
                inorderTraversal(
                        new TreeNode(
                                2,
                                new TreeNode(1),
                                new TreeNode(3))));
    }

    private static class TreeNode 
    {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        
        TreeNode(int val, TreeNode left, TreeNode right) 
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root == null) return list;
        Stack<TreeNode> stack = new Stack<>();
        while(root != null || !stack.empty()){
            while(root != null){
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            list.add(root.val);
            root = root.right;
            
        }
        return list;
    }
}
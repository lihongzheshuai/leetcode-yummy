package com.coderli.leetcode.algorithms.easy;

/**
 * Given a binary tree, find its maximum depth.
 * <p>
 * The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 *
 * @author OneCoder 2017-11-14 23:20
 */
public class MaximumDepthOfBinaryTree {

    public static void main(String[] args) {
        MaximumDepthOfBinaryTree maximumDepthOfBinaryTree = new MaximumDepthOfBinaryTree();
        TreeNode tree = maximumDepthOfBinaryTree.new TreeNode(1);
        TreeNode subNodeLeft = maximumDepthOfBinaryTree.new TreeNode(2);
        TreeNode subNodeRight = maximumDepthOfBinaryTree.new TreeNode(2);
        subNodeLeft.left = maximumDepthOfBinaryTree.new TreeNode(3);
        subNodeLeft.right = maximumDepthOfBinaryTree.new TreeNode(4);
        subNodeRight.left = maximumDepthOfBinaryTree.new TreeNode(4);
        subNodeRight.right = maximumDepthOfBinaryTree.new TreeNode(3);
        tree.left = subNodeLeft;
        tree.right = subNodeRight;
        System.out.println(maximumDepthOfBinaryTree.maxDepth(tree));
    }


    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int maxLeft = maxDepth(root.left);
        int maxRight = maxDepth(root.right);
        int maxChild = maxLeft >= maxRight ? maxLeft : maxRight;
        return maxChild + 1;
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }
}

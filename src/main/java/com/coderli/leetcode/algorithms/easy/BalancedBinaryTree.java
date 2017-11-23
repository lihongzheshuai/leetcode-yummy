package com.coderli.leetcode.algorithms.easy;

/**
 * Given a binary tree, determine if it is height-balanced.
 * <p>
 * For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
 * of every node never differ by more than 1.
 *
 * @author OneCoder 2017-11-23 22:05
 */
public class BalancedBinaryTree {

    public static void main(String[] args) {
        BalancedBinaryTree balancedBinaryTree = new BalancedBinaryTree();
        TreeNode tree = balancedBinaryTree.new TreeNode(1);
        TreeNode subNodeLeft = balancedBinaryTree.new TreeNode(2);
        TreeNode subNodeRight = balancedBinaryTree.new TreeNode(2);
        subNodeLeft.left = balancedBinaryTree.new TreeNode(3);
        subNodeLeft.right = balancedBinaryTree.new TreeNode(4);
        subNodeRight.left = balancedBinaryTree.new TreeNode(4);
        subNodeRight.right = balancedBinaryTree.new TreeNode(3);
        tree.left = subNodeLeft;
        tree.right = subNodeRight;
        System.out.println(balancedBinaryTree.isBalanced(tree));
    }

    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        int leftSubTreeHeight = treeHeight(root.left);
        int rightSubTreeHeight = treeHeight(root.right);
        int differ = leftSubTreeHeight - rightSubTreeHeight;
        if ( differ > 1 || differ < -1) {
            return false;
        }
        return isBalanced(root.left) && isBalanced(root.right);
    }

    private int treeHeight(TreeNode tree) {
        if (tree == null) {
            return 0;
        }
        int leftSubHeight = treeHeight(tree.left);
        int rightSubHeight = treeHeight(tree.right);
        return leftSubHeight >= rightSubHeight ? leftSubHeight + 1: rightSubHeight + 1;
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

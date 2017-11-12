package com.coderli.leetcode.algorithms.easy;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
 * <p>
 * For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
 * <p>
 * 1
 * / \
 * 2   2
 * / \ / \
 * 3  4 4  3
 * But the following [1,2,2,null,3,null,3] is not:
 * 1
 * / \
 * 2   2
 * \   \
 * 3    3
 * Note:
 * Bonus points if you could solve it both recursively and iteratively.
 *
 * @author OneCoder 2017-11-11 21:27
 */
public class SymmetricTree {

    public static void main(String[] args) {
        SymmetricTree symmetricTree = new SymmetricTree();
        SymmetricTree.TreeNode tree = symmetricTree.new TreeNode(1);
        tree.left = symmetricTree.new TreeNode(2);
        tree.right = symmetricTree.new TreeNode(2);
        System.out.println(symmetricTree.isSymmetric(tree));
    }

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        TreeNode leftSide = root.left;
        TreeNode rightSide = root.right;
        Stack<TreeNode> leftStack = new Stack<>();
        while (leftSide != null) {
            leftStack.add(leftSide);
            if (leftSide.left != null) {
            }
        }

        leftSide = leftSide.left;
        rightSide = rightSide.right;
        return false;
    }

    // recursively
    public boolean isSymmetricRecursively(TreeNode root) {
        if (root == null) {
            return true;
        }
        return compare(root.left, root.right);
    }

    private boolean compare(TreeNode leftSide, TreeNode rightSide) {
        if (leftSide == null && rightSide == null) {
            return true;
        }
        if (leftSide == null || rightSide == null) {
            return false;
        }
        if (leftSide.val != rightSide.val) {
            return false;
        }
        return compare(leftSide.left, rightSide.right) && compare(leftSide.right, rightSide.left);
    }

    public class TreeNode {
        int val;
        SymmetricTree.TreeNode left;
        SymmetricTree.TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

}

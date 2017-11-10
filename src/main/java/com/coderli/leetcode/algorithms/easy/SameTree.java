package com.coderli.leetcode.algorithms.easy;

/**
 * Given two binary trees, write a function to check if they are the same or not.
 * <p>
 * Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input:<br>
 * 1         1
 * / \       / \
 * 2   3     2   3
 * <p>
 * [1,2,3],   [1,2,3]
 * <p>
 * Output: true
 * <p></p>
 * Example 2:
 * <p>
 * Input:
 * 1         1
 * /           \
 * 2             2
 * <p>
 * [1,2],     [1,null,2]
 * <p>
 * Output: false
 * <p>
 * Example 3:
 * <p>
 * Input:
 * 1         1
 * / \       / \
 * 2   1     1   2
 * <p>
 * [1,2,1],   [1,1,2]
 * <p>
 * Output: false
 *
 * @author OneCoder 2017-11-10 23:01
 */
public class SameTree {

    public static void main(String[] args) {
        SameTree sameTree = new SameTree();
        TreeNode oneRoot = sameTree.new TreeNode(1);
        oneRoot.left = sameTree.new TreeNode(2);
        TreeNode twoRoot = sameTree.new TreeNode(1);
        oneRoot.right = sameTree.new TreeNode(2);
        System.out.println(sameTree.isSameTree(oneRoot, twoRoot));
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        if (p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
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

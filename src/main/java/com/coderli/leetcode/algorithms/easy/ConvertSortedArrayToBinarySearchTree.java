package com.coderli.leetcode.algorithms.easy;

/**
 * Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 *
 * @author li.hzh 2017-11-16 11:51
 */
public class ConvertSortedArrayToBinarySearchTree {

    public static void main(String[] args) {
        ConvertSortedArrayToBinarySearchTree convert = new ConvertSortedArrayToBinarySearchTree();
        printTreeMidOrder(convert.sortedArrayToBST(new int[]{2, 3, 4, 5, 7, 8, 9}));
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        int left = 0;
        int right = nums.length;
        int mid = left + (right - left) / 2;
        TreeNode tree = new TreeNode(mid);
        tree.left = sortedArrayToBST(left, mid, nums, tree);
        tree.right = sortedArrayToBST(mid + 1, right, nums, tree);
        return tree;
    }

    private TreeNode sortedArrayToBST(int from, int to, int[] nums, TreeNode parent) {
        return null;
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    private static void printTreeMidOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        if (node.left != null) {
            printTreeMidOrder(node.left);
        }
        System.out.print(node.val + " ");
        if (node.right != null) {
            printTreeMidOrder(node.right);
        }

    }
}

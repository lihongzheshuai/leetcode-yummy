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
        printTreeMidOrder(convert.sortedArrayToBST(new int[]{0}));
        printTreeMidOrder(convert.sortedArrayToBST(new int[]{1, 3}));
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        if (nums.length == 1) {
            return new TreeNode(nums[0]);
        }
        int left = 0;
        int right = nums.length - 1;
        int mid = left + (right - left) / 2;
        TreeNode tree = new TreeNode(nums[mid]);
        tree.left = sortedArrayToBST(left, mid - 1, nums, tree);
        tree.right = sortedArrayToBST(mid + 1, right, nums, tree);
        return tree;
    }

    private TreeNode sortedArrayToBST(int from, int to, int[] nums, TreeNode parent) {
        if (from >= to) {
            return new TreeNode(nums[from]);
        }
        int mid = from + (to - from) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = sortedArrayToBST(from, mid - 1, nums, node);
        node.right = sortedArrayToBST(mid + 1, to, nums, node);
        return node;
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

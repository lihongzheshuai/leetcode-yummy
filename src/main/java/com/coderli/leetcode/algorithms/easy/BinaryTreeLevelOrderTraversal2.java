package com.coderli.leetcode.algorithms.easy;

import java.util.*;

/**
 * Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
 * level by level from leaf to root).
 * <p>
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 * 3
 * / \
 * 9  20
 * /  \
 * 15   7
 * return its bottom-up level order traversal as:
 * [
 * [15,7],
 * [9,20],
 * [3]
 * ]
 *
 * @author OneCoder 2017-11-15 20:47
 */
public class BinaryTreeLevelOrderTraversal2 {

    public static void main(String[] args) {
        BinaryTreeLevelOrderTraversal2 binaryTreeLevelOrderTraversal2 = new BinaryTreeLevelOrderTraversal2();
        TreeNode tree = binaryTreeLevelOrderTraversal2.new TreeNode(3);
        TreeNode nineNode = binaryTreeLevelOrderTraversal2.new TreeNode(9);
        TreeNode twentyNode = binaryTreeLevelOrderTraversal2.new TreeNode(20);
        TreeNode fifteenNode = binaryTreeLevelOrderTraversal2.new TreeNode(15);
        TreeNode sevenNode = binaryTreeLevelOrderTraversal2.new TreeNode(7);
        tree.left = nineNode;
        tree.right = twentyNode;
        nineNode.left = fifteenNode;
        twentyNode.right = sevenNode;
        System.out.println(binaryTreeLevelOrderTraversal2.levelOrderBottom(tree));
    }

    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> levelNodeQueue = new LinkedList<>();
        levelNodeQueue.add(root);
        int levelCount = 1;
        int nextLevelCount = 0;
        List<Integer> levelList = new ArrayList<>();
        while (!levelNodeQueue.isEmpty()) {
            TreeNode curNode = levelNodeQueue.poll();
            levelList.add(curNode.val);
            levelCount--;
            if (curNode.left != null) {
                levelNodeQueue.add(curNode.left);
                nextLevelCount++;
            }
            if (curNode.right != null) {
                levelNodeQueue.add(curNode.right);
                nextLevelCount++;
            }
            if (levelCount == 0) {
                result.add(levelList);
                levelList = new ArrayList<>();
                levelCount = nextLevelCount;
                nextLevelCount = 0;
            }

        }
        Collections.reverse(result);
        return result;
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

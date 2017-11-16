package com.coderli.leetcode.algorithms.easy;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

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
        System.out.println(binaryTreeLevelOrderTraversal2.levelOrderBottomWithRecursion(tree));
    }

    public List<List<Integer>> levelOrderBottomWithRecursion(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root != null) {
            List<TreeNode> currentLevel = new ArrayList<>();
            currentLevel.add(root);
            scanNode(currentLevel, result);
        }
        return result;
    }

    private void scanNode(List<TreeNode> levelTreeNodes, List<List<Integer>> result) {
        if (levelTreeNodes == null || levelTreeNodes.isEmpty()) {
            return;
        }
        List<TreeNode> treeNodes = new ArrayList<>(levelTreeNodes.size() * 2);
        List<Integer> valueList = new ArrayList<>(levelTreeNodes.size());
        for (TreeNode node : levelTreeNodes) {
            if (node.left != null) {
                treeNodes.add(node.left);
            }
            if (node.right != null) {
                treeNodes.add(node.right);
            }
            valueList.add(node.val);
        }
        scanNode(treeNodes, result);
        result.add(valueList);
    }

    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> result = new LinkedList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> levelNodeQueue = new LinkedList<>();
        levelNodeQueue.add(root);
        while (!levelNodeQueue.isEmpty()) {
            int size = levelNodeQueue.size();
            List<Integer> levelList = new ArrayList<>(size);
            for (int i = 0; i < size; i++) {
                TreeNode curNode = levelNodeQueue.poll();
                levelList.add(curNode.val);
                if (curNode.left != null) {
                    levelNodeQueue.add(curNode.left);
                }
                if (curNode.right != null) {
                    levelNodeQueue.add(curNode.right);
                }
            }
            result.addFirst(levelList);
        }
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

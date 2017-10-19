package com.coderli.leetcode.algorithms.easy;


/**
 * Merge two sorted linked lists and return it as a new list.
 * The new list should be made by splicing together the nodes of the first two lists.
 *
 * @author li.hzh 2017-10-19
 */
public class MergeTwoSortedLists {

    public static void main(String[] args) {
        MergeTwoSortedLists mergeTwoSortedLists = new MergeTwoSortedLists();
        ListNode first = mergeTwoSortedLists.new ListNode(1);
        first.next = mergeTwoSortedLists.new ListNode(3);
        ListNode second = mergeTwoSortedLists.new ListNode(2);
        second.next = mergeTwoSortedLists.new ListNode(4);
//        print(mergeTwoSortedLists.mergeTwoLists(first, second));
        print(mergeTwoSortedLists.mergeTwoListsWithRecursion(first, second));
    }


    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        ListNode firstNode = null;
        ListNode lastNode = null;
        if (l1.val >= l2.val) {
            lastNode = firstNode = l2;
            l2 = l2.next;
        } else {
            lastNode = firstNode = l1;
            l1 = l1.next;
        }
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                lastNode.next = l2;
                break;
            }
            if (l2 == null) {
                lastNode.next = l1;
                break;
            }
            if (l1.val >= l2.val) {
                lastNode.next = l2;
                l2 = l2.next;
                lastNode = lastNode.next;
            } else {
                lastNode.next = l1;
                l1 = l1.next;
                lastNode = lastNode.next;
            }
        }
        return firstNode;
    }

    public ListNode mergeTwoListsWithRecursion(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        ListNode firstNode = null;
        if (l1.val >= l2.val) {
            firstNode = l2;
            firstNode.next = mergeTwoListsWithRecursion(l1, l2.next);
        } else {
            firstNode = l1;
            firstNode.next = mergeTwoListsWithRecursion(l1.next, l2);
        }
        return firstNode;
    }

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    private static void print(ListNode list) {
        while (list != null) {
            System.out.println(list.val);
            list = list.next;
        }
    }
}

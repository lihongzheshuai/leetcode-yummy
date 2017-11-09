package com.coderli.leetcode.algorithms.easy;

/**
 * Given a sorted linked list, delete all duplicates such that each element appear only once.
 * <p>
 * For example,
 * Given 1->1->2, return 1->2.
 * Given 1->1->2->3->3, return 1->2->3.
 *
 * @author li.hzh 2017-11-09 12:43
 */
public class RemoveDuplicatesFromSortedList {

    public static void main(String[] args) {
        RemoveDuplicatesFromSortedList remove = new RemoveDuplicatesFromSortedList();
        RemoveDuplicatesFromSortedList.ListNode first = remove.new ListNode(1);
        RemoveDuplicatesFromSortedList.ListNode second = remove.new ListNode(1);
        first.next = second;
        second.next = remove.new ListNode(2);
        print(remove.deleteDuplicates(first));
        first.next = second;
        second.next = remove.new ListNode(1);;
        print(remove.deleteDuplicates(first));
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode currentNode = head;
        ListNode preNode = null;
        while (currentNode != null) {
            if (preNode == null) {
                preNode = currentNode;
            } else {
                if (preNode.val == currentNode.val) {
                    preNode.next = currentNode.next;
                } else {
                    preNode = currentNode;
                }
            }
            currentNode = currentNode.next;
        }
        return head;
    }

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    private static void print(RemoveDuplicatesFromSortedList.ListNode list) {
        while (list != null) {
            System.out.println(list.val);
            list = list.next;
        }
    }
}

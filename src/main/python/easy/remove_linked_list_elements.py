# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre_node = None
        cur_node = head
        while cur_node is not None:
            if cur_node.val == val:
                if pre_node is None:
                    head = head.next
                else:
                    pre_node.next = cur_node.next
            else:
                pre_node = cur_node
            cur_node = cur_node.next
        return head
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# author li.hzh
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        slow = fast = headA
        is_headA = True
        while fast is not None:
            slow = slow.next
            if faster.next is not None:
                faster = faster.next.next
            elif is_headA:
                faster = headB
                is_headA = False
            else:
                return None
            if slow is faster:
                break
        if faster is None:
            return None
        slow = headA
        while slow is not faster:
            slow = slow.next
            faster = faster.next
        return slow

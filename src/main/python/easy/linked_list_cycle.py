# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow, faster = head, head.next
        while faster is not None:
            slow = slow.next
            if faster.next is not None:
                faster = faster.next.next
            else:
                return False
            if slow is faster:
                return True
        return False

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(1)
two = ListNode(2)
two.next = head
head.next = two

print(Solution().hasCycle(head))

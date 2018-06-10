# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head
        is_odd = True
        while fast:
            if fast.next:
                fast = fast.next.next
                is_odd = False
            else:
                fast = fast.next
            slow = slow.next





node_1 = ListNode(1)
node_2 = ListNode(1)
node_3 = ListNode(2)
node_4 = ListNode(1)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
Solution().isPalindrome(node_1)

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Note: Do not modify the linked list.
#
# Follow up:
# Can you solve it without using extra space?

# author li.hzh

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 假设链表中环外节点长度为L, 环内节点长度为C。则有：0 <= L; 0 <= C。例如：
        # a - > b - > c - > | d -> e ->f -> g  - >(d)，此时 L= 3， C = 4。
        # 现在考虑有环的情况，现有一快一慢两个指针，慢的每次走一个节点，快的每次两个，则有，慢节点进入环，需要L步，
        # 而此时，快节点已经在环内走了L步。处在环内的 L% C = K的位置。因此，第一次相遇还需要C-K步, 相遇在C-K的位置。
        # 再每次相遇都需要C步。因此，若能求得K。则在第一次相遇的位置，再走K步，即为初始位置。
        # 因此，第一次相遇的步数为L + C- K = X(可得）, 以后每次相遇需要C步（两次相遇可得),

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

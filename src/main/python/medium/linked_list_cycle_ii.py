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
        # 此时 fast 应该在环内的 L % C = K 的位置。对应上例，就是 3 % 4 = 3 （d + 3 = g）的位置。因此，从环内看，
        # 相聚还需要 C - K = 4 - 3 = 1步。因此，第一次相遇在d + 1 = e的位置。此时，走到环的初始位，需要 C - (C - K) = K = 3步。
        # 那么问题就变成了，怎么得到这个K。我们简单思考，当L < C时，显然L = K。当 L > C 时，我们想象成两个每次都一步的指针，一个从头，
        # 一个在环内K位行走。当走各走nC步时，环内回到原地。从原点出发的距离环的入口正好还差K步，因此，不论如何，二者必将在入口处相遇。
        # 入口位的节点就找到了
        if head is None:
            return None
        slow = faster = head
        while faster is not None:
            slow = slow.next
            if faster.next is not None:
                faster = faster.next.next
            else:
                return None
            if slow is faster:
                break
        if faster is None:
            return None
        slow = head
        while slow is not faster:
            slow = slow.next
            faster = faster.next
        return slow


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c

d = ListNode(4)
c.next = d
e = ListNode(5)
d.next = e
f = ListNode(6)
e.next = f
g = ListNode(7)
f.next = g
g.next = d
print(Solution().detectCycle(a))

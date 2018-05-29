# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 迭代法
class SolutionIteratively:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre_node = None
        while head is not None:
            pre_node, head.next, head = head, pre_node, head.next
        return pre_node


# 递归法
class SolutionRecursively:
    def reverseTail(self, pre, cur):
        if cur.next:
            SolutionIteratively().reverseTail(cur, cur.next)
        else:
            cur.next = pre
            return cur

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return SolutionRecursively.reverseTail(None, None, head)


node_5 = ListNode(5)
node_4 = ListNode(4)
node_4.next = node_5
node_3 = ListNode(3)
node_3.next = node_4
node_2 = ListNode(2)
node_2.next = node_3
node_1 = ListNode(1)
node_1.next = node_2

solution = SolutionIteratively()
result = solution.reverseList(node_1)
print(result)

result_rec = SolutionRecursively().reverseList(node_1)
print(result_rec)

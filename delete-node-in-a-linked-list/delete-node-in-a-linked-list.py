# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # this is not a good problem since it doesn't convay itself in non trivial manner
        node.val = node.next.val
        node.next = node.next.next
        
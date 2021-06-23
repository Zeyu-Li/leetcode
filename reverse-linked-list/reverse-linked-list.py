# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while (current):
            new = current.next
            # update pointers
            current.next = previous
            previous = current
            current = new
            
        return previous
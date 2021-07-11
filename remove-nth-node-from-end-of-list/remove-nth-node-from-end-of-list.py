# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # edge cases
        if not head:
            return None
        if not head.next:
            return None
        
        current = head
        size = 0
        while current:
            current = current.next
            size+=1
            
        # print(size)
        # if max
        if size == n:
            return head.next
        
        one_before = head
        for _ in range(size-n-1):
            one_before = one_before.next
            
        # remove
        one_before.next = one_before.next.next
        
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # trival cases
        if not head or left == right:
            return head
        
        dummy = previous = ListNode(None)
        dummy.next = head
        # get to left
        for _ in range(left-1):
            previous = previous.next
            
        current = previous.next
        for _ in range(right-left):
            new = previous.next
            # update pointers
            previous.next = current.next
            current.next = current.next.next
            previous.next.next = new
            
        return dummy.next
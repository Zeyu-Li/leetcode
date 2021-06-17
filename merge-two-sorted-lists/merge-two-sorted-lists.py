# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        top = bottom = ListNode()
        while l1 and l2:
            if (l1.val < l2.val):
                bottom.next = l1
                l1 = l1.next
            else:
                bottom.next = l2
                l2 = l2.next
            bottom = bottom.next
                
        # append the rest
        bottom.next = l1 if l1 else l2
        
        return top.next

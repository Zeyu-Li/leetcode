# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # answer
        l3 = ListNode()
        a = ""
        current = l1
        while current:
            a=str(current.val)+a
            current = current.next
            
        b=""
        current = l2
        while current:
            b=str(current.val)+b
            current = current.next
            
        # print(a,b)
        return_str = str(int(a) + int(b))[::-1]
        # print(return_str)
        # return linked list
        current = l3
        for index, char in enumerate(return_str):
            current.val = int(char)
            if index != len(return_str) - 1:
                current.next = ListNode()
                current = current.next
            
        return l3

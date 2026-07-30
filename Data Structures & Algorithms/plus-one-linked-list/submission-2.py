# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        number = 0
        node = head

        while node:
            number = number*10 + node.val
            node = node.next

        number += 1
        dummy = ListNode(0)
        current = dummy
        for digit in str(number):
            current.next = ListNode(int(digit))
            current = current.next
            
        return dummy.next
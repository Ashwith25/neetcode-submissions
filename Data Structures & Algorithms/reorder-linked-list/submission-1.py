# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        previous = None

        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        if previous:
            previous.next = None

        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node


        first = head
        second = prev
        while first and second:

            tmp1 = first.next
            tmp2 = second.next
            if tmp1:
                first.next = second
                second.next = tmp1
            else:
                first.next = second

            first = tmp1
            second = tmp2
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

        # print(number)
        number += 1

        new_node = head

        for idx, i in enumerate(str(number)):
            new_node.val = i
            print(new_node.val)
            if not new_node.next and idx==len(str(number))-2:
                new_node.next = ListNode(i)
            new_node = new_node.next

        return head
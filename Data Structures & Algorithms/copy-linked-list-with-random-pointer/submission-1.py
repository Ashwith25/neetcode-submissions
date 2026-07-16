"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        map = {}
        current = head

        while current:
            tmp = Node(current.val)
            map[current] = tmp
            current = current.next

        current = head
        res = map[head]
        temp = res
        while current:
            if current.next:
                temp.next = map[current.next]
            if current.random:
                temp.random = map[current.random]
            current = current.next
            temp = temp.next

        return res

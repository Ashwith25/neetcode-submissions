class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        res = temp
        carry = 0
        while l1 or l2 or carry:
            num1, num2 = 0, 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            tmp = num1 + num2 + carry
            carry = tmp // 10
            tmp = tmp % 10
            res.next = ListNode(tmp)
            res = res.next

        return temp.next
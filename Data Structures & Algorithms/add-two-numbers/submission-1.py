# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 123 456 =>
        carry = 0

        curr1 = l1
        curr2 = l2
        dummy = ListNode(-1)
        curr3 = dummy
        while curr1 and curr2:
            add = (curr1.val + curr2.val + carry)
            total = add % 10
            carry = add // 10

            curr3.next = ListNode(total)
            curr3 = curr3.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            add = curr1.val + carry
            total = add % 10
            carry = add // 10
            curr3.next = ListNode(total)
            curr3 = curr3.next
            curr1 = curr1.next
        while curr2:
            add = curr2.val + carry
            total = add % 10
            carry = add // 10
            curr3.next = ListNode(total)
            curr3 = curr3.next
            curr2 = curr2.next
        
        if carry > 0:
           curr3.next = ListNode(carry) 

        return dummy.next
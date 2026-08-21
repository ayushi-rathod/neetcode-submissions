# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        newCurr = None
        l3 = None
        carry  = 0

        while curr1 or curr2:
            total = (curr1.val if curr1 != None else 0) + (curr2.val if curr2 != None else 0) + carry
            carry = total // 10
            node = ListNode(total % 10)

            if l3 == None:
                l3 = node
                newCurr = node
            else:
                newCurr.next = node
                newCurr = newCurr.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if carry > 0:
            newCurr.next = ListNode(carry)
            

        return l3

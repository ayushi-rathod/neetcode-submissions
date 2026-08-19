# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        if count - n == 0:
            return head.next

        curr = head
        count2 = 1
        while curr:
            if count2 == count - n:
                curr.next = curr.next.next
            count2 += 1
            curr = curr.next
        return head
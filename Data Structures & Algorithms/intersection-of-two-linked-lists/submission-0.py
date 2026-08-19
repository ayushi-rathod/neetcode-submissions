# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hset = set()
        list1 = headA
        while list1:
            if list1 not in hset:
                hset.add(list1)
                list1 = list1.next
        list2 = headB
        while list2:
            if list2 in hset:
                return list2
            list2 = list2.next
        return None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        p1, p2 = None, s.next
        s.next = None
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        first, second = head, p1
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
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
        c = {None:None}
        cur = head
        while cur:
            c[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = c[cur]
            copy.next = c[cur.next]
            copy.random = c[cur.random]
            cur = cur.next

        return c[head]
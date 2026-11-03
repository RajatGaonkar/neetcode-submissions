# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        q.append((root, -float('inf')))

        while q:
            node, m = q.popleft()
            if node.val >= m:
                res += 1
            if node.left:
                q.append((node.left, max(node.val, m)))
            if node.right:
                q.append((node.right, max(node.val, m)))
        return res
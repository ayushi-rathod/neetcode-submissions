# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        max_level = 0

        while stack:

            node, level = stack.pop()
            max_level = max(max_level, level)

            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))

        return max_level+1
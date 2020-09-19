# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.helper(root, L, R, 0)
    
    def helper(self, node, left, right, total):
        if node is None:
            return total
        
        if left <= node.val <= right:
            total += node.val
            total = self.helper(node.left, left, right, total)
            total = self.helper(node.right, left, right, total)
        
        if node.val < left:
            total = self.helper(node.right, left, right, total)
        if node.val > right:
            total = self.helper(node.left, left, right, total)
        
        return total

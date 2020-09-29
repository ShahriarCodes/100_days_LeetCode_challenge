# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        depth = 0
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                                
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            depth += 1
            result.append(sum(level)/len(level))
            level = []
            queue = next_queue
            next_queue = []
        return depth    
    
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)
        
        l_diameter = self.diameterOfBinaryTree(root.left)
        r_diameter = self.diameterOfBinaryTree(root.right)
        
        fd  = max(l_height + r_height , max(l_diameter, r_diameter))
        
        return fd
        
    

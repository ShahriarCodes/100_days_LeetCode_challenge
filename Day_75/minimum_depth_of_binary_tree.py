# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
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
                print('inner loop level',level) 
                
                if root.left is None and root.right is None:
                    depth += 1
                    return depth
                
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            depth += 1
            print('outer loop level',level)
            result.append(sum(level)/len(level))
            level = []
            queue = next_queue
            next_queue = []
        return depth    

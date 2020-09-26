# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
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
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result[::-1]
                    
                 


# class Queue(object):
#     def __init__(self):
#         self.items = []
    
#     def enqueue(self, item):
#         self.items.insert(0, item)
    
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop()
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1].val
    
#     def __len__(self):
#         return self.size()
    
#     def size(self):
#         return len(self.items)
    
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return 
        
#         queue = Queue()
#         queue.enqueue(root)
        
#         traversal = ''
#         while len(queue) > 0:
#             traversal += str(queue.peek()) + '-'
#             node = queue.dequeue()
            
#             if node.left:
#                 queue.enqueue(node.left)
#             if node.right:
#                 queue.enqueue(node.right)
        
#         print(traversal.split('-'))
#         return traversal
            
            
        
        
        
        
        
        
        
        
        
        
        

    
    
    

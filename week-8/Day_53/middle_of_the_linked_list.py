# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print(head)
        prev_node = head
        c = 0
        while prev_node.next:
            print(prev_node.val)
            prev_node = prev_node.next
            c+= 1
        c += 1
        print(prev_node.val, c)
        
        if c %2 == 0:
            n = int(c/2) 
        if c %2 != 0:
            n = int(c/2)
        
        prev_node = head
        c = 0
        while prev_node.next:
            # print(prev_node.val)
            if c == n:
                break
            prev_node = prev_node.next
 
            c+= 1
            
        print(prev_node)
        return prev_node
            
            
            
            

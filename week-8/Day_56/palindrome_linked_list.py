# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def isPalindrome(self, head: ListNode) -> bool:
        if not(head) or not(head.next): return True
        
        # Function for reversing the linked list
        def reverseLL(head):
            node, next_node, node.next = head, head.next, None
            while next_node:
                next_node.next, node, next_node = node, next_node, next_node.next                
            return node
              
        # Find the middle node
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        head1 = reverseLL(slow.next)
        while head and head1:
            if head.val!=head1.val: return False
            head, head1 = head.next, head1.next
        
        return True
        

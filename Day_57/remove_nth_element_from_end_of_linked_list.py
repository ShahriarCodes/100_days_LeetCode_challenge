# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)   
        dummy.next = head
        p, f = dummy, dummy
        
        c = 0
        string = 'f not reached'
        while f and f.next:
            c += 1
            f = f.next
            if c > n:
                p = p.next
                
            
        p.next = p.next.next
            
        
        return dummy.next
                

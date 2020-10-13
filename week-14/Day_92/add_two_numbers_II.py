# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node = l1
        l2_node = l2
        l1_str = ''
        l2_str = ''
        while l1_node or l2_node:
            if l1_node:
                l1_str += str(l1_node.val)
                l1_node = l1_node.next
            if l2_node:
                l2_str += str(l2_node.val)
                l2_node = l2_node.next
        print(l1_str,l2_str)
        summ = str(int(l1_str) + int(l2_str))
        
        head  = ListNode()
        prev = head
        # new.val = 1
        for i,num in enumerate(summ):
                prev.val = num
                if i< len(summ)-1:
                    new = ListNode()
                    prev.next = new
                    prev = prev.next
                if i == len(summ)-1:
                    prev.next = None


        return head
        
            

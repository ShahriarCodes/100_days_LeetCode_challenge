# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        lst = []
        node = head
        while node:
            if node.val != val:
                lst.append(node.val)
            node = node.next
        
        
        cur = dummy = ListNode(0)
        for num in lst[0:]:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
 
# O(n) time, O(1) space
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        current_node = ListNode(-1)
        current_node.next = head
        head = current_node
        
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next 
        return head.next 
 

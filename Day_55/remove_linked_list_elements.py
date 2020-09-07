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
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        node = head
        acc = 0
        while True:
            # node = node.next
            slow = slow.next
            fast = fast.next.next
            acc += 1
            if fast.next == None and fast != None:
                # node.next = None
                break
            if fast ==
        
        slow_reversed = self.reverseList(slow)
        
        print('head ::  ', head)
        print('slow :: ', slow)      
        print('slow_reversed :: ', slow_reversed)

        new_acc = 0
        while True:
            new_acc +=1
                
            if new_acc <= acc:
                if head.val == slow_reversed.val:
                    head = head.next
                    slow_reversed = slow_reversed.next
                    
                else:
                    return False
                    break
            else:
                break
        return True
    

            
            

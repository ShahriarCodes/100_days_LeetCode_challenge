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
        # dummy = ListNode(-1)
        # dummy.next = head
        fast = head
        slow = head
        node = head
        acc = 0
        while True:
            # node = node.next
            slow = slow.next
            fast = fast.next.next
            acc += 1
            
            #odd case
            if fast.next == None:
                case = 1
                break
                
            #even case
            if fast.next.next == None:
                case =  0
                break
        
        if case == 1:
            reverse = self.reverseList(slow) #odd
        if case == 0: 
            reverse = self.reverseList(fast) #even
            
        print('head ::  ', head)
        print('fast ::  ', fast)
        print('slow :: ', slow)      
        print('reverse :: ', reverse)

        new_acc = 0
        while True:
            new_acc +=1
                
            if new_acc < acc:
                if head.val == reverse.val:
                    head = head.next
                    reverse = reverse.next
                    
                else:
                    return False
                    break
            else:
                break
        return True
    

            
            

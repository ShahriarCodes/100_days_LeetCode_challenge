class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_last_node = l1
        l1_last_node_val = '{}'.format(l1_last_node.val)
        while l1_last_node.next:
            l1_last_node = l1_last_node.next
            l1_last_node_val += '{}'.format(l1_last_node.val)
        
        l2_last_node = l2
        l2_last_node_val = '{}'.format(l2_last_node.val)
        while l2_last_node.next:
            l2_last_node = l2_last_node.next
            l2_last_node_val += '{}'.format(l2_last_node.val)
        
        summation = str(int(l1_last_node_val[::-1]) + int(l2_last_node_val[::-1]))[::-1]
        
        head_node = ListNode()
        head_node.val = summation[0]
        if len(summation)>1:
            last_node = head_node
            for i in range(1, len(summation)):
                new_node = ListNode()
                new_node.val = summation[i]
                last_node.next = new_node
                last_node = new_node

        return head_node

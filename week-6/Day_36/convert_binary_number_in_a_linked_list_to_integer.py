# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        itr = head
        llstr = ''
        while itr:
            llstr += str(itr.val)

            itr = itr.next
        print(llstr)

        return int(llstr, 2)

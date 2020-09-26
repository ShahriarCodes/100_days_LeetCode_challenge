# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA , nodeB = headA, headB
        l1, l2 = 0 , 0
        while nodeA or nodeB:
            if nodeA != None:
                l1 += 1
                nodeA = nodeA.next
            if nodeB != None:
                l2 += 1
                nodeB = nodeB.next
        
        # print(l1, l2)
        d = l1 - l2
        
        nodeA , nodeB = headA, headB
        c = 0
        intersection = None
        while nodeA and nodeB:
            if c < abs(d):
                if d > 0:
                    nodeA = nodeA.next
                elif d < 0:
                    nodeB = nodeB.next
            
            if c >= abs(d):
                #check memory location
                if id(nodeA) == id(nodeB):
                    intersection = nodeA
                    break
                else:
                    nodeA = nodeA.next
                    nodeB = nodeB.next
            c += 1
        return intersection
                    
                    
        
        

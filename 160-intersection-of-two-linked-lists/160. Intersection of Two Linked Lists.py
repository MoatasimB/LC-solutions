# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ogA = headA
        ogB = headB
        
        while headA and headB:

            headA = headA.next
            headB = headB.next
        
        cnt = 0

        finishedFirst = None
        while headA:
            finishedFirst = "B"
            headA = headA.next
            cnt += 1
        

        while headB:
            finishedFirst = "A"
            headB = headB.next
            cnt += 1
        
        headA = ogA
        headB = ogB

        if finishedFirst == "A":
            for _ in range(cnt):
                headB = headB.next
        else:
            for _ in range(cnt):
                headA = headA.next
        

        while headA and headB:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None





            
          
            
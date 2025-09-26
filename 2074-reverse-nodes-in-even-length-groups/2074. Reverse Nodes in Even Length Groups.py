# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(curr, endNode):
            prev = None
            lastNode = curr #2
            while prev != endNode:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            return prev, lastNode #6 , 2

        groupCount = 1

        count = 0
        finalNode = None
        curr = head 
        prevHead = head
        while curr:
            count += 1

            if count == groupCount:
                if groupCount % 2 == 0:
                    nextNode = curr.next
                    nodeAfterPrev, lastNode = rev(prevHead.next, curr)
                    prevHead.next = nodeAfterPrev
                    lastNode.next = nextNode
                    prevHead = lastNode
                    
                    curr = nextNode
                    count = 0
                    groupCount += 1
                    continue
                else:
                    prevHead = curr #5
                    count = 0
                    groupCount += 1
            
            if curr.next == None:
                finalNode = curr

            curr = curr.next

        
        if count > 0 and count != groupCount:
            if count % 2 == 0:
                nextNode = None
                nodeAfterPrev, lastNode = rev(prevHead.next, finalNode)
                prevHead.next = nodeAfterPrev
                lastNode.next = nextNode

        return head

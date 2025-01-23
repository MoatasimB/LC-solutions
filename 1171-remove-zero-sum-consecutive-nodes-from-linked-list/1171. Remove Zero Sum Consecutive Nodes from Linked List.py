# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mpp = {}
        dummy = ListNode(0, head)
        mpp[0] = dummy

        curr = dummy.next
        s = 0

        while curr:
            s += curr.val


            if s in mpp:
                prev = mpp[s]
                curr = prev.next


                p = s + curr.val

                while p!= s:
                    del mpp[p]
                    curr = curr.next
                    p += curr.val
                
                prev.next = curr.next
            
            else:
                mpp[s] = curr
            
            curr = curr.next
        return dummy.next
        #     mpp[s] = curr
        #     curr = curr.next
        
        # s = 0
        # curr = dummy

        # while curr:
        #     s += curr.val
        #     curr.next = mpp[s].next
        #     curr = curr.next
        
        # return dummy.next

        



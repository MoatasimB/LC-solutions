# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
    def getRandom(self) -> int:
        node = None

        curr = self.head
        i = 1
        while curr:
            x = random.randint(0, i - 1)

            if x == i - 1:
                node = curr
            
            curr = curr.next
            i +=1 
        
        return node.val




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
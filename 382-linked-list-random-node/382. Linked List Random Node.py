# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.len = 0
        curr = head
        while curr:
            self.len +=1 
            curr = curr.next
        self.head = head
    def getRandom(self) -> int:
        x = random.randint(0, self.len - 1)
        # print(x)
        count = 0
        curr = self.head
        while count < x and curr:
            curr = curr.next
            count += 1
        
        return curr.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
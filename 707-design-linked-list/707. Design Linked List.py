class MyLinkedList:
    class ListNode:
        def __init__ (self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.length = 0
        self.head = None
        

    def get(self, index: int) -> int:
        if index> self.length - 1:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.length +=1
        node = ListNode(val, self.head)
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            # self.length +=1
            # node = ListNode(val, self.head)
            # self.head = node
        else:
            curr = self.head
            for _ in range(self.length - 1):
                curr = curr.next
            node = ListNode(val, None)
            curr.next = node
            self.length +=1
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length - 1:
            return
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node = ListNode(val, curr.next)
            curr.next = node
            self.length +=1


        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return
        
        if index == 0:
            self.head = self.head.next
            self.length -=1
            return
        
        dummy = ListNode(0, self.head)
        curr = self.head

        for _ in range(index - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        self.length -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# 6 1 2 0 4 
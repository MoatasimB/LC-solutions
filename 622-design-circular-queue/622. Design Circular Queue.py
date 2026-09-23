class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.len == self.k:
            return False
        prevNode = self.tail.prev
        node = Node(value)
        self.tail.prev = node
        node.next = self.tail

        prevNode.next = node
        node.prev = prevNode
        
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.len -= 1
        return True
        

    def Front(self) -> int:
        return self.head.next.val
        


    def Rear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
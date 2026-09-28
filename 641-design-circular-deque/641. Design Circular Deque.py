class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        nextNode = self.head.next
        node = Node(value)
        self.head.next = node
        node.prev = self.head
        
        node.next = nextNode
        nextNode.prev = node
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        prevNode = self.tail.prev
        node = Node(value)
        self.tail.prev = node
        node.next = self.tail

        prevNode.next = node
        node.prev = prevNode
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        nextNode = self.head.next
        self.head.next = nextNode.next
        nextNode.next.prev = self.head
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        prevNode = self.tail.prev
        prevNode.prev.next = self.tail
        self.tail.prev = prevNode.prev
        self.size -=1
        return True
        

    def getFront(self) -> int:
        return self.head.next.val

    def getRear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
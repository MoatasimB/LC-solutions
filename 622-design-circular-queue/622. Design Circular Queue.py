class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.cap == self.k:
            return False
        newNode = Node(value)

        prevNode = self.tail.prev

        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = self.tail
        self.tail.prev = newNode
        
        # nextNode = self.head.next
        # print(newNode.val, nextNode.val)
        # self.head.next = newNode
        # newNode.prev = self.head
        
        # newNode.next = nextNode
        # nextNode.prev = newNode
        self.cap += 1
        # self.pprint()
        return True
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        nodeToRemove = self.head.next
        nextNode = nodeToRemove.next
        self.head.next = nextNode
        nextNode.prev = self.head
        self.cap -= 1
        return True
    def Front(self) -> int:
        return self.head.next.val if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        return self.tail.prev.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.cap == 0
        

    def isFull(self) -> bool:
        return self.cap == self.k
        
    def pprint(self):
        curr = self.head
        while curr:
            print(f"{curr.val} ->")
            curr = curr.next

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        nextNode = self.head.next
        node = Node(val)

        self.head.next = node
        node.prev = self.head

        node.next = nextNode
        nextNode.prev = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        prevNode = self.tail.prev

        node = Node(val)
        
        prevNode.next = node
        node.prev = prevNode

        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        node = Node(val)
        prevNode = curr.prev

        prevNode.next = node
        node.prev = prevNode

        node.next = curr
        curr.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        prevNode = curr.prev
        nextNode = curr.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
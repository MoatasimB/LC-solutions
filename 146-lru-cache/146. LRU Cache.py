class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.mpp = {} #key,node
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node = self.mpp[key]
        self.delete(node)
        self.addFront(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            self.delete(self.mpp[key])
            del self.mpp[key]
        
        node = Node(key, value)
        self.addFront(node)

        self.mpp[key] = node
        if len(self.mpp) > self.cap:
            nodeToDelete = self.tail.prev
            del self.mpp[nodeToDelete.key]
            self.delete(nodeToDelete)


    def addFront(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext

        headNext.prev = node
    
    def delete(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


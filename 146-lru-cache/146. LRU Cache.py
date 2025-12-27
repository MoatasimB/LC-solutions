class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mpp = {} #key : node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        
        node = self.mpp[key]

        self.deleteNode(node)
        self.addNode(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.mpp:
            node = self.mpp[key]
            self.deleteNode(node)
            del self.mpp[key]
        
        newNode = Node(key, value)

        self.mpp[key] = newNode

        self.addNode(newNode)

        if len(self.mpp) > self.cap:
            lruNode = self.tail.prev
            self.deleteNode(lruNode)
            del self.mpp[lruNode.key]
        
    

    def addNode(self, node):

        nextNode = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nextNode
        nextNode.prev = node

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
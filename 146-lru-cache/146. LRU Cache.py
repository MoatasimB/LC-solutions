class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mpp = {}
        

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        
        node = self.mpp[key]
        print('get:', node.val)

        self.removeNode(node)
        self.addNode(node)


        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            self.removeNode(self.mpp[key])
            del self.mpp[key]
        
        node = Node(key, value)

        self.addNode(node)
        self.mpp[key] = node

        if len(self.mpp) > self.cap:
            key = self.tail.prev.key
            lru = self.mpp[key]
            self.removeNode(lru)
            del self.mpp[key]
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
    def addNode(self, node):
        nextNode = self.head.next
        
        node.prev = self.head
        node.next = nextNode
        
        nextNode.prev = node
        self.head.next = node

   



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
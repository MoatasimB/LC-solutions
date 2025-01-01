class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.map = {}
        self.count = 0

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]

        val = node.val
        
        self.delete(node)
        self.addFront(node)

        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            nodeToDelete = self.map[key]
            self.count -=1
            self.delete(nodeToDelete)
            del self.map[key] 
        
        node = Node(key, value)

        self.map[key] = node

        self.addFront(node)

        self.count +=1

        if self.count > self.cap:
            LRUNODE = self.tail.prev

            del self.map[LRUNODE.key]
            self.delete(LRUNODE)
            self.count -= 1



    

    def addFront(self, node):

        nextNode = self.head.next

        self.head.next = node
        node.next = nextNode

        nextNode.prev = node
        node.prev = self.head
    
    def delete(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
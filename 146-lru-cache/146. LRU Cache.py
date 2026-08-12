class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1, -1)
        self.mpp = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node = self.mpp[key]
        ans = node.val

        self.remove(node)
        self.add(node)
        return ans
        

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            node = self.mpp[key]
            self.remove(node)
        
        node = Node(key, value)
        self.add(node)
        self.mpp[key] = node

        if len(self.mpp) > self.cap:
            removeNode = self.tail.prev
            self.remove(removeNode)
            del self.mpp[removeNode.key]
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def add(self, node):
        prevNode = self.head
        nextNode = self.head.next

        node.prev = prevNode
        prevNode.next = node

        node.next = nextNode
        nextNode.prev = node

    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
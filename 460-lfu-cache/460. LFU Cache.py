class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.useCount = 1

class LRU:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def addNode(self, node):
        nextNode = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nextNode
        nextNode.prev = node
    
    def removeLRU(self):
        LRUnode = self.tail.prev
        self.removeNode(LRUnode)
        return LRUnode
    
    def isEmpty(self):
        return self.head.next == self.tail
    

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.levels = defaultdict(LRU) #freq : LRU
        self.min = 0
        self.nodes = {} #key : node
        
    def updateNode(self, node):
        #increment this nodes freq counter
        currLevel = node.useCount
        nextLevel = node.useCount + 1
        node.useCount += 1

        currLRU = self.levels[currLevel]
        currLRU.removeNode(node)

        if currLRU.isEmpty():
            if self.min == currLevel:
                self.min += 1

        self.levels[nextLevel].addNode(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        val = node.val

        self.updateNode(node)

        return val
        

    def put(self, key: int, value: int) -> None:

        if key in self.nodes:
            node = self.nodes[key]
            node.val = value

            self.updateNode(node)
        else:
            if len(self.nodes) == self.cap:
                minLevel = self.levels[self.min]
                removedNode = minLevel.removeLRU()
                del self.nodes[removedNode.key]
            
            #add new node
            node = Node(key, value)
            self.min = 1
            firstLevel = self.levels[1]

            firstLevel.addNode(node)
            self.nodes[key] = node
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self,key, val, next, prev):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.size = 0
        self.head = Node(-1,-1, None, None)
        self.tail = Node(-1,-1, None, None)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        ans = node.val

        self.delete(node)
        self.add(node)

        return ans

        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.size -= 1
        
        self.dic[key] = Node(key,value, None, None)
        node = self.dic[key]

        self.add(node)

        self.size +=1

        if self.size > self.cap:
            del self.dic[self.tail.prev.key]
            self.delete(self.tail.prev)
            self.size -= 1

    
    def add(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        node.prev = self.head

        nextNode.prev = node
    

    def delete(self, node):
        PrevNode = node.prev
        nextNode = node.next

        PrevNode.next = nextNode
        nextNode.prev = PrevNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
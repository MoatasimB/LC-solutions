class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




class MyHashSet:

    def __init__(self):
        self.lst = [Node(-1) for _ in range(10**3)]
    
    def getHash(self, key):
        return key % (len(self.lst))

    def add(self, key: int) -> None:
        idx  = self.getHash(key)
        node = self.lst[idx]
        while node.next:
            if node.next.val == key:
                return
            node = node.next
        
        newNode = Node(key)
        node.next = newNode
        

    def remove(self, key: int) -> None:
        idx  = self.getHash(key)
        node = self.lst[idx]
        while node.next:
            if node.next.val == key:
                break
            node = node.next
        if node.next:
            nextNode = node.next.next
            node.next = nextNode

    def contains(self, key: int) -> bool:
        idx  = self.getHash(key)
        node = self.lst[idx]
        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
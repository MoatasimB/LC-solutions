class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class Bucket:
    def __init__(self):
        self.head = Node(-1, -1)
    
    def add(self, key, val):

        curr = self.head

        while curr.next:
            if curr.next.key == key:
                curr.next.val = val
                return
            curr = curr.next
        
        newNode = Node(key, val)
        curr.next = newNode
    
    def get(self, key):
        curr = self.head

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1
    
    def remove(self, key):
        curr = self.head

        while curr.next:
            if curr.next.key == key:
                break
            curr = curr.next
        
        if curr.next:
            nextNode = curr.next.next
            curr.next = nextNode


class MyHashMap:

    def __init__(self):
        self.lst = [Bucket() for _ in range(10**3)]

    def getHash(self, key):
        return key % (len(self.lst))
    def put(self, key: int, value: int) -> None:
        bucket = self.lst[self.getHash(key)]
        bucket.add(key, value)

    def get(self, key: int) -> int:
        bucket = self.lst[self.getHash(key)]
        return bucket.get(key)

    def remove(self, key: int) -> None:
        bucket = self.lst[self.getHash(key)]
        bucket.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
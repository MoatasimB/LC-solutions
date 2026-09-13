class Node:
    def __init__(self, level):
        self.next = None
        self.prev = None
        self.keys = set()
        self.level = level

class AllOne:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.strings = {} #key : node it currently is in
        

    def inc(self, key: str) -> None:
        if key not in self.strings:
            if self.head.next.level != 1:
                self.addNewGroup(self.head, 1)
            firstLevel = self.head.next
            firstLevel.keys.add(key)
            self.strings[key] = firstLevel 
        else:
            currGroup = self.strings[key]
            newLevel = currGroup.level + 1
            currGroup.keys.remove(key)

            if currGroup.next.level != newLevel:
                self.addNewGroup(currGroup, newLevel)
            newGroup = currGroup.next

            if len(currGroup.keys) == 0:
                self.removeNode(currGroup)

            newGroup.keys.add(key)
            self.strings[key] = newGroup
            


        

    def dec(self, key: str) -> None:
        currGroup = self.strings[key]
        newLevel = currGroup.level - 1
        currGroup.keys.remove(key)
        if newLevel == 0:
            del self.strings[key]
            
        else: 
            if currGroup.prev.level != newLevel:
                self.addNodePrev(currGroup, newLevel)
            newGroup = currGroup.prev
            self.strings[key] = newGroup
            newGroup.keys.add(key)
        
        if len(currGroup.keys) == 0:
                self.removeNode(currGroup)
    

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        maxNode = self.tail.prev
        for key in maxNode.keys:
            return key

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        minNode = self.head.next
        for key in minNode.keys:
            return key
    def addNewGroup(self, prevNode, val):
        nextNode = prevNode.next
        node = Node(val)
        
        prevNode.next = node
        node.prev = prevNode

        node.next = nextNode
        nextNode.prev = node
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def addNodePrev(self, nextNode, val):
        prevNode = nextNode.prev
        node = Node(val)
        prevNode.next = node
        node.prev = prevNode

        node.next = nextNode
        nextNode.prev = node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
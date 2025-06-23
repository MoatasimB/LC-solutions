class Node: 
    def __init__(self, level):
        self.level = level
        self.set = set()
        self.next = None
        self.prev = None

#H <-> 1.    5             T
class AllOne:

    def __init__(self):
        self.node_mpp = {} #string_key: node (node.level = count)
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def inc(self, key: str) -> None:
        #if key doesnt exist:
        if key not in self.node_mpp:
            #We first check if we have a count=1 node

            #if not we make the node
            if self.head.next.level != 1:
                nextNode = self.head.next
                prevNode = self.head
                newNode = Node(1)
                self.addNode(prevNode, nextNode, newNode)
            #if so we add it to the mpp and add it to the nodes set
            #don't need an else cause we always add it
            node_to_add_key_in = self.head.next 
            node_to_add_key_in.set.add(key)
            self.node_mpp[key] = node_to_add_key_in

        #the key exists so we have to remove it from its current node
        #and go to the next node
        else:
            node_with_key = self.node_mpp[key]

            #now we check if the next count node is there or not
            if node_with_key.next.level != node_with_key.level + 1:
                #if it is not there we have to create the next new node
                next_level = node_with_key.level + 1
                new_node = Node(next_level)
                prevNode = node_with_key
                nextNode = node_with_key.next
                self.addNode(prevNode, nextNode, new_node)
            
        #then we add it to the new node
            new_node_with_key = node_with_key.next
            self.node_mpp[key] = new_node_with_key
            node_with_key.set.remove(key)
            new_node_with_key.set.add(key)

            #if the node we moved from is empty we remove it
            if len(node_with_key.set) == 0:
                prevNode = node_with_key.prev
                nextNode = node_with_key.next
                self.delNode(prevNode, nextNode)

        

    def dec(self, key: str) -> None:

        node_with_key = self.node_mpp[key]
        #if we are in level 1 then we can just get rid of the key
        if node_with_key.level == 1:
            node_with_key.set.remove(key)
            del self.node_mpp[key]
        else:
            #if the prev level exists we move it to it
            if node_with_key.prev.level != node_with_key.level - 1:
            #if it does not exist we create it and then we move the node
                level = node_with_key.level - 1
                nextNode = node_with_key
                prevNode = node_with_key.prev
                newNode = Node(level)

                self.addNode(prevNode, nextNode, newNode)
        
            #we move to the prev level
            prevLevel = node_with_key.prev
            prevLevel.set.add(key)
            node_with_key.set.remove(key)
        
            self.node_mpp[key] = prevLevel

        #if the level is empty then we remove it
        if len(node_with_key.set) == 0:
            prevNode = node_with_key.prev
            nextNode = node_with_key.next
            self.delNode(prevNode, nextNode)
        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        
        maxNode = self.tail.prev

        for el in maxNode.set:
            return el
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        
        minNode = self.head.next

        for el in minNode.set:
            return el

    def addNode(self, prevNode, nextNode, newNode):
        newNode.next = nextNode
        nextNode.prev = newNode
        newNode.prev = prevNode
        prevNode.next = newNode
    
    def delNode(self, prevNode, nextNode):
        prevNode.next = nextNode
        nextNode.prev = prevNode

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
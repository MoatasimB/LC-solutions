class Node:
    def __init__(self, count): #contains all the strings with count = val
        self.count = count
        self.strings = set()
        self.next = None
        self.prev = None


class AllOne:

    def __init__(self):
        #create head -> min ..... max -> tail
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.nodeGroups = {} #key : node it is in

        self.stringCounts = defaultdict(int) #key : count
        

    def inc(self, key: str) -> None:
        if key not in self.nodeGroups:
            
            #check if we dont have a 1 group
            if self.head.next.count != 1:
                #then create a 1 group
                self.addNewGroup(self.head, 1)

            #add string to a 1 group
            group1 = self.head.next
            group1.strings.add(key)
            # stringCounts[key] += 1
            self.nodeGroups[key] = group1

        else:
            currentGroup = self.nodeGroups[key]

            #check if the next doesnt group exists and then add if the case
            if currentGroup.next.count != currentGroup.count + 1:
                self.addNewGroup(currentGroup, currentGroup.count + 1)
            
            #now add this string to this new group and remove from old
            currentGroup.strings.remove(key)
            
            newGroup = currentGroup.next
            newGroup.strings.add(key)
            # stringCounts[key] += 1
            self.nodeGroups[key] = newGroup

            #We also want to see if the oldGroup is empty now, if it is we remove it
            if len(currentGroup.strings) == 0:
                self.removeGroup(currentGroup)

    def dec(self, key: str) -> None:
        currentGroup = self.nodeGroups[key]

        # if it is in group1 we just remove it from dic and ll
        if currentGroup.count == 1:
            #remove from dic
            del self.nodeGroups[key]
            #remove from ll
            currentGroup.strings.remove(key)

            #if we have nothing in this group we remove it
            if len(currentGroup.strings) == 0:
                self.removeGroup(currentGroup)
        
        else:
        #if it is another random group check if previous one exists
            if currentGroup.count != currentGroup.prev.count + 1:
                self.addPrevGroup(currentGroup, currentGroup.count - 1)
            
            currentGroup.strings.remove(key)
            newGroup = currentGroup.prev

            newGroup.strings.add(key)

            self.nodeGroups[key] = newGroup
            if len(currentGroup.strings) == 0:
                self.removeGroup(currentGroup)


        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        for s in self.tail.prev.strings:
            return s
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        for s in self.head.next.strings:
            return s
    
    def addNewGroup(self, prevNode, val):
        #Adds a new group
        node = Node(val)

        nextNode = prevNode.next
        prevNode.next = node
        nextNode.prev = node

        node.next = nextNode
        node.prev = prevNode
    
    def addPrevGroup(self, nextNode, val):
        node = Node(val)

        prevNode = nextNode.prev

        prevNode.next = node
        nextNode.prev = node

        node.prev = prevNode
        node.next = nextNode


    
    def removeGroup(self, group):

        prevNode = group.prev
        nextNode = group.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    

    

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
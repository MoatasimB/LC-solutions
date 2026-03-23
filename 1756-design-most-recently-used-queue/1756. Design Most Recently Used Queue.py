class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MRUQueue:

    def __init__(self, n: int):
        self.n = n
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.idxToNodeMap = {}
        
        curr = self.head

        for i in range(1, n + 1):
            newNode = Node(i)
            nextNode = curr.next
            curr.next = newNode
            newNode.prev = curr

            newNode.next = nextNode
            nextNode.prev = newNode
            self.idxToNodeMap[i] = newNode
            curr = curr.next

    def fetch(self, k: int) -> int:

        node = self.idxToNodeMap[k]
        # print(node.prev.val if node.prev else None, node.val, node.next.val if node.next else None)
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        # print("______________________________________")
        curr = prevNode
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node


        curr = curr.next

        for idx in range(k, self.n + 1):
            self.idxToNodeMap[idx] = curr
            curr = curr.next
        
            


        return node.val
    


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
class Node:
    def __init__(self, char):
        self.val = char
        self.next = None
        self.prev = None
class TextEditor:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.head
        

    def addText(self, text: str) -> None:
        for ch in text:
            newNode = Node(ch)
            afterCursor = self.cursor.next
            self.cursor.next = newNode
            newNode.prev = self.cursor
            newNode.next = afterCursor
            afterCursor.prev = newNode
            self.cursor = self.cursor.next

    def deleteText(self, k: int) -> int:
        curr = self.cursor.next
        count = 0
        while k > 0 and self.cursor != self.head:
            self.cursor = self.cursor.prev
            k -= 1
            count += 1
        self.cursor.next = curr
        curr.prev = self.cursor
        return count
    
    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.cursor != self.head:
            self.cursor = self.cursor.prev
            k -= 1
        s = self.getText()
        return s

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.cursor.next != self.tail:
            self.cursor = self.cursor.next
            k -= 1
        s = self.getText()
        return s
    
    def getText(self):
        k = 10
        curr = self.cursor
        string = []
        while k > 0 and curr != self.head:
            string.append(curr.val)
            curr = curr.prev
            k -= 1
        x = "".join(string[::-1])
        return x

    def pprint(self):
        curr = self.head.next
        while curr!= self.tail:
            print(curr.val, end= "")
            curr = curr.next
        print('\n')

            
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
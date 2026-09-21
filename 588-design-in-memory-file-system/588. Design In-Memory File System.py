class Node:
    def __init__(self, val):
        self.val = val
        self.children = {} #all the sub directories/files : node obj of their rep
        self.file = False
        self.fileContent = []

class FileSystem:

    def __init__(self):
        self.head = Node("/")
        

    def ls(self, path: str) -> List[str]:
        curr = self.head

        path = path.split("/")
        
        for d in path:
            if d == "":
                continue
            
            curr = curr.children[d]
        
        if curr.file:
            return [curr.val]
        
        ans = []
        print(curr.children)
        for child in curr.children:
            ans.append(child)
        
        return sorted(ans)

        

    def mkdir(self, path: str) -> None:
        
        curr = self.head

        path = path.split("/")

        for d in path:
            if d == "":
                continue
            
            if d not in curr.children:
                curr.children[d] = Node(d)
            
            curr = curr.children[d]


        

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.head

        path = filePath.split("/")

        for d in path:
            if d == "":
                continue
            
            if d not in curr.children:
                curr.children[d] = Node(d)
            
            curr = curr.children[d]
        
        curr.file = True
        curr.fileContent.append(content)
        

    def readContentFromFile(self, filePath: str) -> str:
        
        curr = self.head

        path = filePath.split("/")

        for d in path:
            if d == "":
                continue
            
            # if d not in curr.children:
            #     curr.children[d] = Node(d)
            
            curr = curr.children[d]
        
        return "".join(curr.fileContent)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
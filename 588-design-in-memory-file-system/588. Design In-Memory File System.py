class Node:
    def __init__(self, name):
        self.children = {}
        self.isFile = False
        self.subDir = SortedList()
        self.contents = []
        self.name = name

class FileSystem:

    def __init__(self):
        self.root = Node("/")
        

    def ls(self, path: str) -> list[str]:
        curr = self.root
        
        path = path.split("/")
        for x in path:
            if x:
                curr = curr.children[x]
        
        if curr.isFile:
            return [curr.name]
        else:
            return list(curr.subDir)

        

    def mkdir(self, path: str) -> None:
        curr = self.root
        
        path = path.split("/")
        # print(path)
        for x in path:
            if x:
                if x not in curr.children:
                    curr.children[x] = Node(x)
                    curr.subDir.add(x)
                curr = curr.children[x]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        
        path = filePath.split("/")
        
        for x in path:
            if x:
                if x not in curr.children:
                    curr.children[x] = Node(x)
                    curr.subDir.add(x)
                curr = curr.children[x]

        curr.isFile = True
        curr.contents.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        path = filePath.split("/")
        
        for x in path:
            if x:
                curr = curr.children[x]
        
        return "".join(curr.contents)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
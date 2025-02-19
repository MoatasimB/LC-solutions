class FileSystem:

    def __init__(self):
        self.paths = {}
        self.parents = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == '/':
            return False
        
        lst = path.split('/')
        lst = [item for item in lst if item]
        parentPath = "/".join(lst[:len(lst) - 1])
        curr = parentPath + '/' + lst[-1]
        # print(curr, parentPath, self.paths)

        if len(lst) == 1:
            if curr[1:] in self.paths:
                return False
            self.paths[curr[1:]] = value
            return True

        if parentPath not in self.paths or curr in self.paths:
            return False
        
        # del self.paths[parentPath]

        self.paths[curr] = value

        return True


        # print(lst)
        # if len(lst) > 1:
        #     for item in lst:
        #         if item not in self.paths:
        #             return False
        # self.paths["".join(lst)] = value
        # print(self.paths)
        # return True
        
    def get(self, path: str) -> int:
        lst = path.split('/')
        lst = [item for item in lst if item]
        x = "/".join(lst)
        if x in self.paths:
            return self.paths[x]
        
        return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
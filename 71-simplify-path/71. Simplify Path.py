class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')
        print(path)
        stack = []

        for i in range(len(path)):
            if path[i] == "..":
                if stack:
                    stack.pop()
                continue
            if path[i] == "." or path[i]=='':
                continue
            stack.append(path[i])
        
        return '/' + "/".join(stack)
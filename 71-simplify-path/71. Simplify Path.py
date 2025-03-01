class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        s = []

        for i in range(len(path)):
            if 0 == len(path[i]) or path[i] == ".":
                continue
            if path[i] == "..":
                if s:
                    s.pop()
                continue
            s.append(path[i])
        
        return "/" + "/".join(s)

                
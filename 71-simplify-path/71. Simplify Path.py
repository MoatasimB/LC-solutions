class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        string = path.split('/')
        print(string)
        
        for group in string:
            
            if group == "." or group=="":
                continue
            elif group == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(group)
        
        ans = '/'.join(stack)
        
            
        return "/" + ans
        
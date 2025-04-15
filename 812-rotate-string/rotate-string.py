class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        q = deque()

        for ch in s:
            q.append(ch)
        while "".join(q) != goal:
            ch = q.popleft()
            q.append(ch)
            if "".join(q) == s:
                return False
        
        return True
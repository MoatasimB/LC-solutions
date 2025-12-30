class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        m = len(goal)
        s = s + s

        for i in range(n):
            if s[i:i + m] == goal:
                return True
        return False



        q = deque()

        for ch in s:
            q.append(ch)
        while "".join(q) != goal:
            ch = q.popleft()
            q.append(ch)
            if "".join(q) == s:
                return False
        
        return True
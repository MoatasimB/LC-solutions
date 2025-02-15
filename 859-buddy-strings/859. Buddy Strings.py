class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if Counter(s) != Counter(goal):
            return False
        
        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False
        
        diffCount = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffCount +=1
            if diffCount > 2:
                return False
        
        return True

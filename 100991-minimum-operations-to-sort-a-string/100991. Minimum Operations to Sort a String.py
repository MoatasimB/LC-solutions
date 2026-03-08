class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)
        t = "".join(sorted(s))
    
        if s == t:
            return 0
        if n == 2:
            return -1
        if s[0] == t[0] or s[-1] == t[-1]:
            return 1

        for i in range(n - 1):
            if s[i] == t[0]:
                return 2
        for i in range(1, n):
            if s[i] == t[-1]:
                return 2
        
            
        return 3

        # "omo"
        # "moo"
       
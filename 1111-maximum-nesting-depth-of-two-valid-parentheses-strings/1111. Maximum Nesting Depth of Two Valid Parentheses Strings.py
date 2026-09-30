class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        ans = []
        n = len(seq)

        depth = 0
        for ch in seq:
            if ch == "(":
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1
        
        return ans
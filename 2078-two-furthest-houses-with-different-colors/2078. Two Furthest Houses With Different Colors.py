class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        ans = float("-inf")

        n = len(colors)

        for i in range(n):
            if n - i < ans:
                break
            color = colors[i]
            for j in range(n - 1, -1, -1):
                color2 = colors[j]
                if color != color2:
                    ans = max(ans, abs(j - i))
        
        return ans
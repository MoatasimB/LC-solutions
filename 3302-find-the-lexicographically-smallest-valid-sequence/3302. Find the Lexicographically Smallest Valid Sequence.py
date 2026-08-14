class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        
        j = m - 1
        last = [0] * m
        for i in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            if j < 0:
                break

        mod = False

        ans = []
        j = 0
        for i in range(n):
            if j == m:
                break
            
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not mod and (j == m - 1 or i < last[j + 1]):
                mod = True
                j += 1
                ans.append(i)
        
        return ans if j == m else []


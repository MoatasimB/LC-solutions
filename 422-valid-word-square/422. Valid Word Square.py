class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        m = len(words)

        for i in range(m):
            for j in range(len(words[i])):
                if j >= m or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        
        return True
   
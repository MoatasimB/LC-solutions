class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        

        j = len(s) - 1

        while j >= 0 and s[j] == ' ':
            j -= 1
        
        ans = 0
        while j >= 0 and s[j] != ' ':
            ans +=1
            j -= 1
        
        return ans
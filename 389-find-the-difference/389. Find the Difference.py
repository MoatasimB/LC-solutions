class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0] * 26

        for i in range(len(t)):
            letters[ord(t[i]) - ord('a')] +=1
        
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] -=1
        
        for i in range(len(letters)):
            if letters[i] == 1:
                return chr(i + ord('a'))

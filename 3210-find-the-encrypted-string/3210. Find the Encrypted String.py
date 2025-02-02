class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        lst = list(s)

        for i in range(len(s)):
            lst[i] = s[(i+k) % len(s)]
        
  
        
        return "".join(lst)

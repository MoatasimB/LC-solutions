class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while columnNumber:
            columnNumber -= 1
            letter_val = chr(columnNumber % 26 + ord('A'))
            ans += letter_val
        
            columnNumber //= 26
        
        return ans[::-1]

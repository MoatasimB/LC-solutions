class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        curr = 0

        while curr < x:
            
            curr = curr * 10 + (x % 10)
            x = x // 10
        

        return curr == x or curr // 10 == x
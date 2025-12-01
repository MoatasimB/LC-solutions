class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        
        curr = 0
        while curr < x:
            digit = x % 10
            x = x // 10
            curr = (curr * 10) + digit
        

        return curr == x or (curr // 10) == x
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        
        num = 0

        while x > num:
            digit = x % 10
            num = num * 10 + digit
            x = x // 10
        
        return x == num or x == num // 10
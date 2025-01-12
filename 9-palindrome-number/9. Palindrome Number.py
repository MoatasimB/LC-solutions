class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        curr = []
        while x:
            digit = x % 10
            x = x // 10
            curr.append(digit)
        
        i = 0
        j = len(curr) - 1


        while i<=j:
            if curr[i] != curr[j]:
                return False
            i +=1
            j-=1
        
        return True
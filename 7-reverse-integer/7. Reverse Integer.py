class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        curr = 0

        while x:
            digit = int(math.fmod(x, 10))

            if curr > INT_MAX // 10 or (curr == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            if curr < INT_MIN // 10 or (curr == INT_MIN // 10 and digit < INT_MIN % 10):
                return 0
            
            curr = curr * 10 + digit
            x = int(x / 10)
        

        return curr
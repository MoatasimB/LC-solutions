class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        sumDigits = 0
        newNum = 0
        power = 0
        while n:
            digit = n % 10
            sumDigits += digit

            n = n // 10

            if digit == 0:
                continue
            newNum += digit * 10**power
            power += 1

        return sumDigits * newNum

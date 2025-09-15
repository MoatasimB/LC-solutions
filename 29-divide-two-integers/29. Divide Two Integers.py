class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = -2**30

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        neg = 2

        if divisor > 0:
            divisor = -divisor
            neg -= 1
        
        if dividend > 0:
            dividend = -dividend
            neg -= 1
        

        

        doubles = []
        powers = []

        currPowerTwo = 1
        while dividend <= divisor:

            doubles.append(divisor)
            powers.append(currPowerTwo)

            if divisor < HALF_MIN_INT:
                break

            currPowerTwo += currPowerTwo
            divisor += divisor
        

        ans = 0
        for i in range(len(doubles) - 1, -1, -1):
            if doubles[i] >= dividend:
                ans += powers[i]

                dividend -= doubles[i] 
        

        return ans if neg != 1 else -ans


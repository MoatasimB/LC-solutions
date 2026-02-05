class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def check(num):
            while num:
                digit = num % 10
                if digit == 0:
                    return False
                num = num // 10
            return True

        for i in range(1, n):
            num1 = i
            num2 = n - i
            if check(num1) and check(num2):
                return [num1, num2]

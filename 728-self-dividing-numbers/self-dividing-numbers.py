class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        ans = []
        for num in range(left, right + 1):
            n = num
            digits = []
            while n:
                digits.append(n % 10)
                n = n // 10
            
            if 0 in digits:
                continue
            flag = True
            for digit in digits:
                if num % digit:
                    flag = False
                    break
            if flag:
                ans.append(num)
        return ans

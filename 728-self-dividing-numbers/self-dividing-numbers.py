class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        ans = []
        for num in range(left, right + 1):
            n = num
            digits = []
            flag = True
            while n > 0:
                if (n % 10) == 0 or num % (n % 10) :
                    flag = False
                    break
                n = n // 10
        
            if flag:
                ans.append(num)
        return ans

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def check(num):
            count = 0
            str_num = str(num)
            for i in range(1, len(str_num) - 1):
                prev = int(str_num[i - 1])
                curr = int(str_num[i])
                next = int(str_num[i + 1])

                if prev < curr and curr > next:
                    count += 1
                if prev > curr and curr < next:
                    count += 1
            return count
        ans = 0
        for num in range(num1, num2 + 1):
            ans += check(num)
        
        return ans

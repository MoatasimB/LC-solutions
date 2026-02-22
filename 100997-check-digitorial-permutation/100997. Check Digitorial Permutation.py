class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        memo = {}

        def getF(x):
            if x in memo:
                return memo[x]
            if x == 0:
                return 1

            ans = x * getF(x - 1)

            memo[x] = ans
            return ans

        total = 0
        curr = n

        while curr:
            digit = curr % 10
            total += getF(digit)
            curr = curr // 10

        if total == n:
            return True

        str_total = str(total)
        str_n = str(n)
        if len(str_total) != len(str_n):
            return False

        need = defaultdict(int)
        for ch in str_total:
            need[ch] += 1

        for ch in str_n:
            if ch not in need:
                return False
            need[ch] -= 1
            if need[ch] < 0:
                return False

        return sum(need.values()) ==0 

        # 541 = 145
        # 514 = 145
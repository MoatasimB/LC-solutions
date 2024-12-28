class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def ss(x):
            ans = 0
            while x:
                ans += (x % 10) **2
                x = x//10
            return ans

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n = ss(n)


        return True
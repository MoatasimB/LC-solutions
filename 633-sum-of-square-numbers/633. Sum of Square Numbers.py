class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c == 2:
        #     return True

        l= 0
        r = int(sqrt(c)) + 1

        for i in range(r):
            n = i

            left = i
            right = r

            while left <= right:
                mid = (right + left) // 2

                if (n*n) + (mid * mid) > c:
                    right = mid - 1
                elif (n*n) + (mid * mid) < c:
                    left = mid + 1
                else:
                    return True
        return False

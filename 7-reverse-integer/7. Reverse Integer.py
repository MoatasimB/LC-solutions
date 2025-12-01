class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res
        
        # MAX_INT = 2**31 - 1
        # MIN_INT = -(2**31)
        
        # maxThresHold = MAX_INT // 10
        # maxThresHoldDigit = MAX_INT % 10

        # minThres = int(MIN_INT / 10)
        # minThresDigit = int(math.fmod(MIN_INT, 10))
        # res = 0

        # while x:
        #     digit = int(math.fmod(x, 10))
        #     x = int(x / 10)

        #     if res * 10 > MAX_INT / 10 or (res * 10 == MAX_INT // 10 and digit > MAX_INT % 10):
        #         return 0
        #     if res * 10 < minThres or (res * 10 == minThres and digit < minThresDigit):
        #         return 0


        #     res = (res * 10) + digit
        
        # return res
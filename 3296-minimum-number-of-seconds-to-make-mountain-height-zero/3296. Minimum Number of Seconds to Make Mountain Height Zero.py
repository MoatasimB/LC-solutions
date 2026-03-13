class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        #  E_{1}^{k} Z * i

        # Z * E_{1}^{k} i <= mid
        # Z * (k)(k + 1) / 2  <= mid
        # (k)(k + 1)  <= 2 * mid / Z
        workerTimes.sort()
        n = len(workerTimes)
        l = min(workerTimes)
        r = workerTimes[-1] * (((mountainHeight) * (mountainHeight + 1)) // 2)
        def canDestroy(time, maxTime):
            l = 0
            r = mountainHeight
            res = 0
            while l <= r:
                amount = (l + r) // 2

                if time * ((amount * (amount + 1)) // 2) <= maxTime:
                    res = amount
                    l = amount + 1
                else:
                    r = amount - 1
            return res
                

        def check(maxTime):
            curr = 0
            for i in range(n):
                curr += canDestroy(workerTimes[i], maxTime)
                if curr >= mountainHeight:
                    return True
            return False


        ans = 0
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

        #can i destroy the mountain in max MID seconds

        #how much can each worker destroy in max MID seconds

    
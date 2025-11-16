class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * n

        for i in range(n):
            curr = stations[i]
            diff[max(0,i - r)] += curr
            if i + r + 1 < n:
                diff[i + r + 1] -= curr
        # [4 0 0 0]
        print(diff)
        def check(mid):
            remaining = k
            diff_copy = diff.copy()
            curr = 0
            for i in range(len(diff_copy)):
                curr += diff_copy[i]
                if curr < mid:
                    need = mid - curr
                    remaining -= need
                    curr += need
                    if i + 2 * r + 1 < n:
                        diff_copy[i + 2 * r + 1] -= need 
            
            return remaining >= 0

  

        # [33, 47, 54, 41, 29]

   
        left = min(stations)
        right = sum(stations) + k
        ans = left
        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans




class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda x : (x[0], -x[1]))

        nums = [x[1] for x in envelopes]
        def find(target):
            l = 0
            r = len(dp) - 1
            ans = len(dp)

            while l <= r:
                mid = (l + r) // 2
                if dp[mid] < target:
                    l = mid + 1
                else:
                    ans = mid
                    r = mid - 1
            
            return ans

        
        dp = []
        for num in nums:
            idx = find(num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        
        return len(dp)

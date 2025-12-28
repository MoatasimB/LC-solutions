class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        nums = [[n, c] for n, c in zip(nums, cost)]
        nums.sort()
        ans = float("inf")
        pref = [0] * n
        pref[0] = nums[0][1]

        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i][1]
        print(nums, pref)
        total = 0
        for i in range(1, n):
            diff = nums[i][0] - nums[0][0]
            total += diff * nums[i][1]
        ans = min(ans, total)

        for i in range(1, n):
            delta = nums[i][0] - nums[i - 1][0]

            #left increases by delta
            leftPrefix = pref[i - 1]
            total += leftPrefix * delta

            #right decreases by delta
            rightPrefix = pref[n - 1] - pref[i - 1]
            total -= rightPrefix * delta

            ans = min(ans, total)
        
        return ans
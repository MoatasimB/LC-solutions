class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key= lambda x: (x[0], -x[1]))
        print(envelopes)
        def find(arr, num):
            if not arr:
                return 0
            l = 0
            r = len(arr) - 1
            ans = len(arr)
            while l<=r:
                mid = (l+r) // 2

                if num > arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    ans = min(ans, mid)
            return ans

        def lis(nums):

            dp = []
            for i in range(len(nums)):
                idx = find(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
            #     for j in range(i):
            #         if nums[j] < nums[i]:
            #             curr = max(curr, 1 + dp[j])
                
            #     dp[i] = curr
            # return max(dp)
        nums = [i[1] for i in envelopes]
        return lis(nums)
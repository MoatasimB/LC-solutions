class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        

        def sw(n):
            counts = defaultdict(int)
            l = 0
            ans = 0

            for r in range(len(nums)):
                counts[nums[r]] += 1

                mpp_len = len(counts)
                
                while l <= r and mpp_len >= n:
                    ans += len(nums) - r
                    counts[nums[l]] -= 1
                    if counts[nums[l]] == 0:
                        del counts[nums[l]]
                    mpp_len = len(counts)
                    l += 1

            return ans
        return sw(k) - sw(k + 1)
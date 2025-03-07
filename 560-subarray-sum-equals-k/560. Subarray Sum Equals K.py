class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mpp = defaultdict(int)
        mpp[0] = 1

        curr = 0
        ans = 0

        for num in nums:
            curr += num
            if (curr - k) in mpp:
                ans += mpp[curr-k]
            mpp[curr] += 1
        
        return ans
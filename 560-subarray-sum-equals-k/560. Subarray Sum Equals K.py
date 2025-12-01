class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        freq = defaultdict(int)
        freq[0] = 1

        curr = 0
        ans = 0
        for i in range(len(nums)):
            curr += nums[i]

            if (curr - k) in freq:
                ans += freq[curr - k]
            
            freq[curr] += 1
        
        return ans

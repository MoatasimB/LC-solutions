class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        seen = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if (nums[i] * nums[j]) in seen:
                    ans += 8 * seen[nums[i] * nums[j]]
                
                seen[nums[i] * nums[j]] += 1
        print(seen)
        return ans
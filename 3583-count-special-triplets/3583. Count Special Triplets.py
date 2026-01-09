class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        total_counts = defaultdict(int)

        for num in nums:
            total_counts[num] += 1
        

        left_counts = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            val = nums[i]
            target = val * 2
            left = 0
            right = 0
            #check left half
            if target in left_counts:
                left = left_counts[target]

            total_counts[val] -= 1
            left_counts[val] += 1

            #check right half
            if target in total_counts:
                right = total_counts[target]
            
            ans += ((left * right) % MOD) % (MOD)
        
        return ans % MOD
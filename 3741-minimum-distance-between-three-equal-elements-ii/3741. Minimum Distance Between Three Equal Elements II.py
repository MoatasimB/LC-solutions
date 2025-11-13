class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num_indices = defaultdict(list)
        
        for i in range(len(nums)):
            num_indices[nums[i]].append(i)

        ans = float("inf")
        for key, val in num_indices.items():
            
            if len(val) >= 3:
                val.sort()
                for i in range(len(val) - 2):
                    one = val[i]
                    two = val[i + 1]
                    three = val[i + 2]
                    ans = min(ans, abs(one - two) + abs(two - three) + abs(one - three))

        return ans if ans != float("inf") else -1
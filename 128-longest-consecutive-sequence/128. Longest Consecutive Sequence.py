class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        ans = 1
        for num in seen:
            if num - 1 not in seen:
                curr = 1
                n = num
                while n + 1 in seen:
                    curr +=1
                    ans = max(ans, curr)
                    n +=1


        return ans

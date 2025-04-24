class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        first = nums[0]

        s = sum(nums)
        n = len(nums)
        ans = float('inf')
        prev = 0
        final = 0
        for i in range(len(nums)):
            prev += nums[i]
            
            x = int(prev / (i + 1))
            y = int((s - prev) / (max(1, n - i - 1)))
            # print(f"{prev}/{i + 1}, {s - prev}/{max(1, n - i - 1)}, {abs(x-y)}")
            if abs(x - y) < ans:
                ans = abs(x - y)
                final = i
        return final

    
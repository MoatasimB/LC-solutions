class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        maxSum = float('-inf')
        curr = 0
        currMin = 0
        totalSum = 0
        minSum = float('inf')

        for num in nums:
            if curr <= 0:
                curr = 0
            curr += num
            maxSum = max(maxSum, curr)

            if currMin >= 0:
                currMin = 0
            currMin += num
            minSum = min(minSum, currMin)

            totalSum += num
        
        if totalSum == minSum:
            return maxSum
        
        return max(maxSum, totalSum - minSum)
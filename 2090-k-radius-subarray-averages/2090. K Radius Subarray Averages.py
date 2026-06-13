class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        ans =[]
        n = len(nums)
        
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        
        
        for i in range(n):
            if i - k < 0 or i + k > n -1:
                ans.append(-1)
            else:
                ans.append((prefix[i+k] - prefix [i-k] + nums[i-k])//(2*k + 1))
        
        return ans
            
        
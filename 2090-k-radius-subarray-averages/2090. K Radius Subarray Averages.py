class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        answer=[]
        n = len(nums) - 1
        
        if k == 0:
            for num in nums:
                answer.append(num)
            return answer
        
        for i in range(len(nums)):
            if i < k or (n - i) < k:
                answer.append(-1)
            # elif i == k:
            #     curr = prefix[i + k]
            #     average = curr // ((k * 2) + 1)
            #     answer.append(average)
            else:
                # curr = prefix[i + k] - prefix[i - (k +1)]
                curr = prefix[i + k] - prefix[i - k] + nums[i -k]

                average = curr // ((k * 2) + 1)
                answer.append(average)
            
        return answer
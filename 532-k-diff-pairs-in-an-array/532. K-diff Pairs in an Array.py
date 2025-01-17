class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:

            mpp = defaultdict(int)

            for num in nums:
                mpp[num] +=1
            
            ans = 0
            for key,val in mpp.items():
                if val >=2:
                    ans +=1
            return ans


        seen = set()
        numsSeen = set()
        ans = 0
        for i in range(len(nums)):

            if (nums[i] - k) in seen and nums[i] not in numsSeen:
                ans +=1
            if (nums[i] + k) in seen and nums[i] not in numsSeen:
                ans +=1
        
            seen.add(nums[i])
            numsSeen.add(nums[i])

        return ans
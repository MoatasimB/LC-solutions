class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        ans = float('inf')
        minDiff = float('inf')

        for i in range(len(nums)):
            curr = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = curr + nums[l] + nums[r]
                print(s)
                diff = abs(target - s)
                if diff < minDiff:
                    minDiff = diff
                    ans = s
                if s > target:
                    r -= 1
                else:
                    l += 1
        
        return ans


        [-4, -1, 1, 2]


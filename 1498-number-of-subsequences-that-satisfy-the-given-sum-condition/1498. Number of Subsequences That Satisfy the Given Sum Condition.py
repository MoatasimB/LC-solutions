class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        # s = sorted([[n,idx] for idx, n in enumerate(nums)])

        def search(start, num):
            end = len(nums) - 1
            ans = -1
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] + num <= target:
                    ans = max(ans, mid)
                    start = mid + 1
                else:
                    end = mid - 1
            
            return ans



        nums.sort()
        ans = 0
        for i in range(len(nums)):
            mmin = nums[i]
            if mmin + mmin > target:
                break
            idx = search(i, mmin)
            if idx == -1:
                break
            # print(i, idx)
            ans += (2 ** (idx - i))
        
        return ans % (10**9 + 7)


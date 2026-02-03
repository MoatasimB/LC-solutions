class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        lst = SortedList()
        ans = []
        for i in range(len(nums)):
            lst.add(nums[i])
            if i >= k:
                lst.remove(nums[i - k])
            if i >= k - 1:
                ans.append(lst[k // 2] if k%2 else (lst[k // 2] + lst[(k // 2) - 1]) / 2)
        
        return ans

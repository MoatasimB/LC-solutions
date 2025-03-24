class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []

        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        i = 0
        j = 0

        while len(ans) < len(nums):
            ans.append(pos[i])
            ans.append(neg[j])
            i+=1
            j += 1
        
        return ans
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i+j].append(nums[i][j])
        
        ans = []


        for i in range(len(diags)):
            for j in range(len(diags[i]) - 1, -1, -1):
                ans.append(diags[i][j])
        
        return ans
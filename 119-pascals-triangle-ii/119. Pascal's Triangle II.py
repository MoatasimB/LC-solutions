class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = [0] * (rowIndex + 1)

        for i in range(len(ans)):
            ans[i] = math.comb(rowIndex, i)
        
        return ans
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        curr = []
        final = []
        for i in range(numRows):
            for j in range(i + 1):
                curr.append(math.comb(i,j))
            final.append(curr)
            curr = []
        
        return final



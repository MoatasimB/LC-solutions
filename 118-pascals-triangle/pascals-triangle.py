class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        curr = [1]

        for i in range(1, numRows):
            prev = ans[-1]
            for j in range(1, i):
                print(prev)
                curr.append(prev[j-1] + prev[j])
            
            curr.append(1)
            ans.append(curr)
            curr = [1]
        
        return ans



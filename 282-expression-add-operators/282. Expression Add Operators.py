class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        ans = []
        def dfs(i, prev, curr, val, exp):
            # print(curr, exp)
            if i == len(num):
                if curr == 0 and val == target:
                    ans.append(exp[1:])
                return
            
            curr = (curr * 10) + int(num[i])

            if curr > 0:
                dfs(i+1, prev, curr, val, exp)
            
            #+
            dfs(i+1, curr, 0 , val + curr, exp + f"+{curr}")

            if exp:
            #-
                dfs(i+1, -curr,0 ,val - curr, exp + f"-{curr}")


                #*
                dfs(i+1, curr * prev, 0 ,val - prev + (curr * prev), exp + f"*{curr}")
        
        dfs(0,0,0,0,"")
        return ans
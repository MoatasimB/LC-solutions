class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        

        #in between I can have no 0/1/8s, one 0, two 0s etc
        # 0,1,8 our completely sym
        mpp = {
            '1':'1',
            '8':'8',
            '6':'9',
            '0':'0',
            '9':'6'
        }
        
        def dfs(n, final_length):
            if n == 1:
                return ['0', '1', '8']
            if n == 0:
                return [""]

            prev = dfs(n-2, final_length)
            ans = []
   
            for num in prev:
                for digit in '01896':
                    if digit == '0' and n == final_length:
                        continue
                    ans.append(digit + num + mpp[digit])
            return ans
        
        return dfs(n, n)









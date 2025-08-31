class Solution:
    def countAndSay(self, n: int) -> str:
        
        def consecutiveNums(nums):
            l = 0
            ans = []
            for r in range(len(nums)):
                if nums[r] != nums[l]:
                    ans.append(str(r - l))
                    ans.append(nums[l])
                    l = r 
            
            if nums[r] == nums[l]:
                ans.append(str(r - l + 1))
                ans.append(nums[l])
            return ans
        
        
        def dfs(i):
            if i == 1:
                return ["1"]
            # if i == 2:
            #     return ["1", "1"]
            prev = dfs(i - 1)
            
            new = consecutiveNums(prev)
            print(new)
            return new
        
        
        return "".join(dfs(n))
    
    

        
      
        
                
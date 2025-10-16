class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        ans = []
        count = 1
        if n % 2 != 0:
            ans.append(0)
            n -= 1
        while n:
            ans.append(count)
            n-=1
            ans.append(-count)
            n-=1
            count +=1
        
        return ans
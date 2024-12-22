class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def check(mid):

            ans = 0 

            for i in range(len(citations)):
                if mid <= citations[i]:
                    ans +=1
            
            return mid <= ans


        l = 0
        r = max(citations)
        ans = 0

        while l <= r:

            mid = (l+r) // 2
            print(l,r,mid)

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
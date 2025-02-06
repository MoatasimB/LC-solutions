class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        a_set = set()
        b_set = set()
        ans = [0] * len(A)
        if A[0] == B[0]:
            ans[0] = 1
        a_set.add(A[0])
        b_set.add(B[0])
        
        for i in range(1, len(A)):
            if A[i] == B[i]:
                ans[i] += 1
            
            if (A[i] in b_set): 
                ans[i] += 1
                
            if B[i] in a_set:
                ans[i] += 1

            ans[i] += ans[i-1]
            a_set.add(A[i])
            b_set.add(B[i])
        
        return ans
        
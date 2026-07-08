class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        
        prefixSum = [int(s[0])]
        n = len(s)
        MOD = 10**9 + 7
        pow10 = [1] * 100001
        for i in range(1, 100001):
            pow10[i] = pow10[i - 1] * 10 % MOD
        for i in range(1, n):
            prefixSum.append(prefixSum[-1] + int(s[i]))

        numsArray = []
        lenArray = []
        curr = 0
        length = 0
        for i in range(n):
            if s[i] != "0":
                curr = ((curr * 10) + int(s[i])) % MOD
                length += 1 
            numsArray.append(curr)
            lenArray.append(length)
        
        def getDigitSum(start, end):
            if start == 0:
                return prefixSum[end]
            return prefixSum[end] - prefixSum[start - 1]
        def getNum(start, end):
            if start == 0:
                return numsArray[end]
            length = lenArray[end] - lenArray[start - 1]
            return (numsArray[end] - (numsArray[start - 1] * pow10[length])) % MOD
        
        

        
        ans = []

        for a, b in queries:
          digitSum = getDigitSum(a, b)
          num = getNum(a, b)
          ans.append((num * digitSum) % MOD)
       
        return ans


        # 1 2 3 4
        # 0 2 4 7

        # 113366610

        # 1 1 12 12 123 123 123 1234

        #start = smallest idx that is greater or equal
        #end = largest idx that is less or equal
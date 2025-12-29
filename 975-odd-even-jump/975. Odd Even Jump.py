class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        oddNext = [0] * n
        evenNext = [0] * n

        stack = []
        for i, num in sorted(enumerate(arr), key = lambda x:x[1]):
            while stack and stack[-1] < i:
                oddNext[stack.pop()] = i
            
            stack.append(i)
        
        stack = []
        for i, num in sorted(enumerate(arr), key = lambda x:x[1], reverse = True):
            while stack and stack[-1] < i:
                evenNext[stack.pop()] = i
            
            stack.append(i)

        oddJumps = [0] * n
        evenJumps = [0] * n

        oddJumps[n - 1] = 1
        evenJumps[n - 1] = 1

        for i in range(n - 2, -1, -1):
            nextOddJump = oddNext[i]
            if oddNext and evenJumps[nextOddJump]:
                oddJumps[i] = 1
            
            nextEvenJump = evenNext[i]
            if evenNext and oddJumps[nextEvenJump]:
                evenJumps[i] = 1
        
        return sum(oddJumps)

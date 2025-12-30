class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        nextOdd = [0] * n
        nextEven = [0] * n

        stack =[]
        for i, num in sorted(enumerate(arr), key=lambda x: x[1]):
            while stack and stack[-1] < i:
                nextOdd[stack.pop()] = i
            stack.append(i)
        stack =[]
        for i, num in sorted(enumerate(arr), key=lambda x: x[1], reverse = True):
            while stack and stack[-1] < i:
                nextEven[stack.pop()] = i
            stack.append(i)
        
        oddJumps = [0] * n
        evenJumps = [0] * n
        oddJumps[n - 1] = 1
        evenJumps[n - 1] = 1

        for i in range(n - 2, -1, -1):
            nextJump = nextOdd[i]
            if nextJump:
                oddJumps[i] = evenJumps[nextJump]
            
            nextJump = nextEven[i]
            if nextJump:
                evenJumps[i] = oddJumps[nextJump]
        
        return sum(oddJumps)
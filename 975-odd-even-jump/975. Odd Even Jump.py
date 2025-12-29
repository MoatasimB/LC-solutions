class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        odd_next = [0] * n
        even_next = [0] * n

        stack = []
        for i, val in sorted(enumerate(arr), key = lambda x : x[1]):
            while stack and stack[-1] < i:
                odd_next[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i, val in sorted(enumerate(arr), key = lambda x : x[1], reverse = True):
            while stack and stack[-1] < i:
                even_next[stack.pop()] = i
            stack.append(i)
        
        odd_next_jump = [0] * n
        even_next_jump = [0] * n
        odd_next_jump[n-1] = 1
        even_next_jump[n-1] = 1

        for i in range(n-2, -1, -1):
            nextJumpOdd = odd_next[i]
            if nextJumpOdd and even_next_jump[nextJumpOdd]:
                odd_next_jump[i] = 1
            
            nextJumpEven = even_next[i]
            if nextJumpEven and odd_next_jump[nextJumpEven]:
                even_next_jump[i] = 1
        
        return sum(odd_next_jump)
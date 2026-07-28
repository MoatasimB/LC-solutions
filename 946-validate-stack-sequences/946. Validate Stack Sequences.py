class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        next = 0

        for i in range(len(pushed)):
            stack.append(pushed[i])

            while stack and stack[-1] == popped[next]:
                stack.pop()
                next +=1

        

        return not stack
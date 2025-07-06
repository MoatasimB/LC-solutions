class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        # pos = ->
        # neg = <-

        stack = []

        for i in range(len(asteroids)):
            ast = asteroids[i]

            while stack and ast < 0 and stack[-1] > 0:
                prev = stack.pop()
                if prev == abs(ast):
                    ast = 0
                elif prev > abs(ast):
                    stack.append(prev)
                    ast = 0
            if ast != 0:
                stack.append(ast)
        
        return stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        # pos = ->
        # neg = <-

        stack = []

        for i in range(len(asteroids)):
            ast = asteroids[i]

            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] > abs(ast):
                    ast = 0
                elif stack[-1] == abs(ast):
                    stack.pop()
                    ast = 0
                    continue
                else:
                    stack.pop()


            if ast != 0:
                stack.append(ast)
        
        return stack
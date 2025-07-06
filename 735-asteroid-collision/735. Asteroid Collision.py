class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #Only way asteroids to collide is if we have one that is going right in our stack
        #And the next one is going left
        #Otherwise it is not possible for asteroids to collide
        #Left is represented by negative and right by positive

        #We can implement a stack and check the last element if it is going right
        #If the curr element is going left and see what happens once they explode

        stack = []

        def Rightmovement(asteroid):
            if asteroid < 0:
                return False
            else:
                return True 

        for i in range(len(asteroids)):
            
            if stack and not Rightmovement(asteroids[i]) and Rightmovement(stack[-1]):
                
                while stack and Rightmovement(stack[-1]) and not Rightmovement(asteroids[i]) and abs(stack[-1]) < abs(asteroids[i]):
                    x = stack.pop()
             
            
                if stack and abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    continue
                
                if not stack or (not Rightmovement(stack[-1]) and not Rightmovement(asteroids[i])):
                    stack.append(asteroids[i])
 
            else:
                
                stack.append(asteroids[i])
        
        return stack
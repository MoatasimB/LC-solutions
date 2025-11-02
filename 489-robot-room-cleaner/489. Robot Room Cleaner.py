# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
    
    #go back -> turn right, turn right, move 
    #reor -> turn right, turn right


        #up (-1,0), right (0,1), down(1,0), left(0,-1)
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        FACES = ["UP", "RIGHT", "DOWN", "LEFT"] 
        seen = set()
        def dfs(r,c, orientation):
            # print(r,c, FACES[orientation])
            # print(seen)
            robot.clean()
            seen.add((r,c))
            for i in range(orientation, orientation + 4):
                dx, dy = dirs[i % 4]
                nr, nc = r + dx, c + dy

                if (nr,nc) not in seen:
                    if robot.move():
                        dfs(nr,nc, i % 4)
                        robot.turnRight()
                    else:
                        robot.turnRight()
                else:
                    robot.turnRight()
            
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        return dfs(0,0,0)

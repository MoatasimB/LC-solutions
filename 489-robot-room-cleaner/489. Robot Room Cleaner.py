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
        
        dirs = [(-1, 0), (0, -1), (1,0), (0,1)]
#up, left, down, right
        seen = set()
        def dfs(r, c, i):
            print(r, c, i)
            robot.clean()
            seen.add((r, c))

            for idx in range(4):
                dx, dy = dirs[(i + idx) % 4]
                nr = r + dx
                nc = c + dy
                if (nr, nc) in seen:
                    robot.turnLeft()
                    continue
                if robot.move():
                    dfs(nr, nc, (i + idx) % 4)
                    robot.turnLeft()
                else:
                    robot.turnLeft()
            
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        
        dfs(0, 0, 0)

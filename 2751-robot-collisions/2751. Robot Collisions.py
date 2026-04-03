class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        robPos = [[i, p] for i, p in enumerate(positions)]

        robPos.sort(key = lambda x : x[1])

        stack = []

        for robot, position in robPos:
            direction = directions[robot]
            health = healths[robot]

            if direction == "R":
                stack.append([robot, direction, health])
            else:
                while stack and stack[-1][1] == "R":
                    prevRobot, prevDirection, prevHealth = stack[-1]

                    if prevHealth == health:
                        stack.pop()
                        health = 0
                        break
                    elif prevHealth > health:
                        stack[-1][2] -= 1
                        health = 0
                        break
                    else:
                        stack.pop()
                        health -= 1
                
                if health > 0:
                    stack.append([robot, direction, health])
        
        robotAndHealth = {}

        for robot, _, health in stack:
            robotAndHealth[robot] = health

        return [robotAndHealth[i] for i in range(len(positions)) if i in robotAndHealth]
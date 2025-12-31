class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        enter = deque() #[time, idx]
        exit = deque() #[time, idx]
        q = deque()
        ans = [0] * n
        for i in range(n):
            q.append([arrival[i], i])

        prev = None #0 enter, 1 exit
        time = 0
        
        while q or enter or exit:
            while q and q[0][0] <= time:
                if state[q[0][1]] == 0:
                    enter.append(q.popleft())
                else:
                    exit.append(q.popleft())

            enterSize = len(enter)
            exitSize = len(exit)

            if enterSize + exitSize == 1:
                if enterSize == 1:
                    enterTime, enterIdx = enter.popleft()
                    ans[enterIdx] = time
                    prev = 0
                else:
                    exitTime, exitIdx = exit.popleft()
                    ans[exitIdx] = time
                    prev = 1
                time += 1
            elif enterSize > 1 and exitSize == 0:
                prev = 0
                while enter:
                    enterTime, enterIdx = enter.popleft()
                    ans[enterIdx] = time
                    time += 1
            
            elif enterSize == 0 and exitSize > 1:
                prev = 1
                while exit:
                    exitTime, exitIdx = exit.popleft()
                    ans[exitIdx] = time
                    time += 1 
            
            elif enterSize >= 1 and exitSize >= 1:
                if prev == None or prev == 1:
                    prev = 1
                    exitTime, exitIdx = exit.popleft()
                    ans[exitIdx] = time
                else:
                    enterTime, enterIdx = enter.popleft()
                    ans[enterIdx] = time
                time += 1
            else:
                time += 1
                prev = None

        return ans


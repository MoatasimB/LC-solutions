class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        
        q = deque()
        ans = [0] * len(arrival)
        for i in range(len(arrival)):
            q.append([arrival[i], i])
        
        t = 0
        prev = -1
        enter = deque()
        exit = deque()
        while q or enter or exit:
            while q and q[0][0] <= t:
                if state[q[0][1]] == 0:
                    enter.append(q.popleft())
                else:
                    exit.append(q.popleft())
            # print(t)
            # print(enter)
            # print(exit)
            if len(enter) + len(exit) == 1:
                if len(enter) == 1:
                    prev = 0
                    ans[enter.popleft()[1]] = t
                else:
                    prev = 1
                    ans[exit.popleft()[1]] = t
                t += 1
            elif len(enter) > 1 and len(exit) == 0:
                prev = 0
                while enter:
                    ans[enter.popleft()[1]] = t
                    t += 1

            elif len(enter) == 0 and len(exit) > 1:
                prev = 1
                while exit:
                    ans[exit.popleft()[1]] = t
                    t += 1
            elif len(enter) >= 1 and len(exit) >= 1:
                if prev == -1:
                    ans[exit.popleft()[1]] = t
                    prev = 1


                elif prev == 0:
                    ans[enter.popleft()[1]] = t
                
                else:
                    ans[exit.popleft()[1]] = t
                
                t += 1
            else:
                prev = -1
                t += 1
        
        return ans


            

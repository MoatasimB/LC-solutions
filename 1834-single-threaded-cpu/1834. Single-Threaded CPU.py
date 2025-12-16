class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        # print(tasks)
        heapq.heapify(tasks)


        toDo = []
        time = tasks[0][0]
        ans = []
        while tasks or toDo:

            while tasks and tasks[0][0] <= time:
                enqTime, procTime, idx = heapq.heappop(tasks)
                heapq.heappush(toDo, [procTime, idx])
            
            if toDo:
                procTime, idx = heapq.heappop(toDo)
                ans.append(idx)
                time += procTime

            if tasks and not toDo:
                time = max(time, tasks[0][0])
        
        return ans

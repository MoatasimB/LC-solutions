class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1
        
        sched = [[-val, key] for key, val in counts.items()]
        heapify(sched)

        q = deque()
        time = 0
        while sched or q:
            if sched:
                task_count, current_task = heapq.heappop(sched)
                if (task_count * -1) - 1> 0:
                    q.append(((task_count * -1) - 1, current_task, time + n))
            if q:
                if q[0][2] <= time:
                    task_count, current_task, t = q.popleft()
                    heapq.heappush(sched, [-task_count, current_task])
            
            time += 1
        
        return time
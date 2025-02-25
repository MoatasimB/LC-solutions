class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        
        counts = [0] * k

        pq = [] #minHeap (finishTime, server)
        free = [i for i in range(k)]
        
        for i, arrivalTime in enumerate(arrival):
            while pq and arrivalTime >= pq[0][0]:
                _, server = heapq.heappop(pq)
                mult = i // k
                # 0 1 2   3 4 5
                # 0 1 2   

                heapq.heappush(free, ((server- i) % k) + i)
            
            if free:
                server = heapq.heappop(free)
                counts[server % k] += 1
                heapq.heappush(pq, (arrivalTime + load[i], server % k))
        

        ans = []
        mmax = -1
        
        for i in range(len(counts)):
            if counts[i] > mmax:
                ans = []
                ans.append(i)
                mmax = counts[i]
            elif counts[i] == mmax:
                ans.append(i)
        
        return ans

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        free = [i for i in range(k)]
        inUse = [] #[endTime, serverID]
        freq = defaultdict(int)
        for i, time in enumerate(arrival):

            while inUse and inUse[0][0] <= time:
                _, serverID = heapq.heappop(inUse)

                heapq.heappush(free, i + (serverID - i) % k)
            
            if free:
                serverID = heapq.heappop(free) % k
                freq[serverID] += 1
                duration = load[i]
                heapq.heappush(inUse, [time + duration, serverID])
        

        ans = []
        maxCount = 0
        for server, count in freq.items():
            if count > maxCount:
                ans = [server]
                maxCount = count
            elif count == maxCount:
                ans.append(server)

        return ans                


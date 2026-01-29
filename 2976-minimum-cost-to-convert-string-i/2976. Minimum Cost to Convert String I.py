class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        graph = defaultdict(list)

        for i in range(len(original)):
            ch1 = original[i]
            ch2 = changed[i]
            w = cost[i]
            graph[ch1].append([ch2, w])
        def findCost(startCh, endCh):
            minHeap = [[0, startCh]]
            dists = [float("inf")] * 26
            dists[ord(startCh) - ord('a')] = 0
            while minHeap:
                c, letter = heapq.heappop(minHeap)
                if letter == endCh:
                    return c
                
                if dists[ord(letter) - ord('a')] < c:
                    continue
                
                for nei, w in graph[letter]:
                    if w + c < dists[ord(nei) - ord('a')]:
                        dists[ord(nei) - ord('a')] = w + c
                        heapq.heappush(minHeap, [w + c, nei])
            
            return -1

        minCosts = defaultdict(int)

        for startCh in "abcdefghijklmnopqrstuvwxyz":
            for endCh in "abcdefghijklmnopqrstuvwxyz":
                curr = findCost(startCh, endCh)
                minCosts[(startCh, endCh)] = curr if curr != -1 else -1

        
        final = 0
        for i in range(len(source)):
            curr = minCosts[(source[i], target[i])]
            if curr == -1:
                return -1
        
            final += curr
        
        return final

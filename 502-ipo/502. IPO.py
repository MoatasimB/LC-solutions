class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        comb = []

        for i in range(len(capital)):
            comb.append([capital[i], profits[i]])
        
        comb.sort()
        heap = []

        i = 0
        while k:
            
            while i < len(comb) and comb[i][0] <= w:
                heapq.heappush(heap, -comb[i][1])
                i+=1

            if not heap:
                break
            
            w += -heapq.heappop(heap)

            k -= 1
        
        return w


        [ [-1,0]]
        [-3, 1], [-2, 1],
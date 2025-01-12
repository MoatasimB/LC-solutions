class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        comb = []

        for i in range(len(capital)):
            comb.append([-profits[i], capital[i]])
        
        heapq.heapify(comb)

        curr = w

        while k:
            waitlist = []
            while comb and comb[0][1] > curr:
                waitlist.append(heapq.heappop(comb))

            if not comb:
                return curr
            projectProfit, cost  = heapq.heappop(comb)

            projectProfit *= -1

            curr  += projectProfit

            for i in range(len(waitlist)):
                heapq.heappush(comb, waitlist[i])

            k -= 1
        
        return curr


        [ [-1,0]]
        [-3, 1], [-2, 1],
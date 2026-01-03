class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        

#         flights = [
#             [0,1,1],
#             [1,0,1],
#             [1,1,0]
#             ]
#         0 -> 1
#         0 -> 2
#         1 -> 0
#         1 -> 2
#         2 -> 0
#         2 -> 1
#         days = [
#             w1, w2, w3
# city 0     [1,  3,  1],
# city 1     [6,  0,  3],
# city 2     [3,  3,  3]
#             ]
        n = len(flights)
        graph = defaultdict(list) #city to city connections
        weeks = len(days[0])
        for i in range(n):
            for j in range(n):
                if flights[i][j] == 1:
                    graph[i].append(j)
        memo = {}
        def dfs(city, k):
            if (city, k) in memo:
                return memo[(city, k)]
            if k == weeks:
                return 0
            
            #choose to stay in city
            stay = days[city][k] + dfs(city, k + 1)

            #go to another city
            move = 0
            for nei in graph[city]:
                move = max(move, days[nei][k] + dfs(nei, k + 1))

            ans = max(stay, move)
            memo[(city, k)] = ans
            return ans

        return dfs(0, 0)
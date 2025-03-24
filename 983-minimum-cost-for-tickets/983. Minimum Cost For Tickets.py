class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        dp = {}
        days_to_buy = set(days)
        def dfs(day):
            if day > days[-1]:
                return 0
            if day in dp:
                return dp[day]
            if day not in days_to_buy:
                return dfs(day + 1)

            # while i < len(days) and days[i] < day:
            #     i += 1
            # if i == len(days):
            #     return 0
            # ans = None
            # if day >= days[i]:
            #     ans = dfs(i+1, day)
            
            # else:
            # one_day = costs[0] + dfs(i+1, days[i]+ 1)
            # seven_day = costs[1] + dfs(i+1, days[i]+ 7)
            thirty_day = costs[2] + dfs(day + 30)
            seven_day = costs[1] + dfs(day + 7)
            one_day = costs[0] + dfs(day + 1)

            ans = min(one_day, seven_day, thirty_day)
            
            dp[day] = ans
            return ans
        
        return dfs(1)
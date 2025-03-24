class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_to_buy = set(days)

        dp = [0] * (days[-1] + 1)
        # i = 0
        # for day in range(1, days[-1] + 1):
        #     if days[i] >=  day:
        #         dp[day] = dp[day - 1]
        #     else:
        #         i += 1
        #         thirty_day = costs[2] + (dp[day - 30] if day - 30 >= 0 else 0)
        #         seven_day = costs[1] + (dp[day - 7] if day - 7 >= 0 else 0)
        #         one_day = costs[0] + (dp[day - 1] if day - 1 >= 0 else 0)

        #         dp[day] = min(thirty_day, seven_day, one_day)
        # return dp[days[-1]]
        
        for day in range(days[-1], 0, -1):
            if day not in days_to_buy:
                dp[day] = dp[day + 1]
            else:
                thirty_day = costs[2] + (dp[day + 30] if day + 30 <= days[-1] else 0)
                seven_day = costs[1] + (dp[day + 7] if day + 7 <= days[-1] else 0)
                one_day = costs[0] + (dp[day +  1] if day + 1 <= days[-1] else 0)

                ans = min(one_day, seven_day, thirty_day)
                
                dp[day] = ans
        # print(dp)
        return dp[1]
        
        dp = {}
        days_to_buy = set(days)
        def dfs(day):
            if day > days[-1]:
                return 0
            if day in dp:
                return dp[day]
            if day not in days_to_buy:
                return dfs(day + 1)

            thirty_day = costs[2] + dfs(day + 30)
            seven_day = costs[1] + dfs(day + 7)
            one_day = costs[0] + dfs(day + 1)

            ans = min(one_day, seven_day, thirty_day)
            
            dp[day] = ans
            return ans
        
        return dfs(1)
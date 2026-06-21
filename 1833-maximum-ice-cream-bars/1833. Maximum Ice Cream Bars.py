class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        bars = [0] * (max(costs) + 1)

        for c in costs:
            bars[c] += 1
        
        ans = 0
        print(bars)
        for i, bar in enumerate(bars):
            if bar > coins:
                return ans
            if i == 0 or bar <= 0:
                continue
            take = min(bar, (coins // i))
            # print(bar, take, coins)
            coins -= take * i
            ans += take
        return ans
            

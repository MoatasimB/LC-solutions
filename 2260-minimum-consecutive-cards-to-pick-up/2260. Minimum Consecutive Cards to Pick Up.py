class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        last_seen = {}

        ans = float("inf")

        for i in range(len(cards)):

            if cards[i] in last_seen:
                if i - last_seen[cards[i]] + 1 < ans:
                    ans = i - last_seen[cards[i]] + 1
            
            last_seen[cards[i]] = i
        

        return ans if ans!= float("inf") else -1
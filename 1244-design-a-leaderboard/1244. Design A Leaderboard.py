class Leaderboard:

    def __init__(self):
        self.maxHeap = []
        self.players = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] += score
        heapq.heappush(self.maxHeap, [-self.players[playerId], playerId])
        

    def top(self, K: int) -> int:
        topK = []
        final = 0
        seen = set()
        while self.maxHeap and len(topK) != K:
            topScore, playerId = heapq.heappop(self.maxHeap)
            topScore *= -1
            if self.players[playerId] == topScore and playerId not in seen:
                seen.add(playerId)
                topK.append([-topScore, playerId])
                final += topScore
        

        for s, i in topK:
            heapq.heappush(self.maxHeap, [s, i])
        return final
        

    def reset(self, playerId: int) -> None:
        self.players[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

# 1: 2
# 2: 1

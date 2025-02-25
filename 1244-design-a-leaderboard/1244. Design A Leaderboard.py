class Leaderboard:

    def __init__(self):
        self.mpp = {}
        self.pq = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.mpp:
            self.mpp[playerId] = score
        else:
            self.mpp[playerId] += score        

    def top(self, K: int) -> int:
        x = sorted(self.mpp.values(), reverse=True)
        
        return sum(x[:K])

    def reset(self, playerId: int) -> None:
        self.mpp[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
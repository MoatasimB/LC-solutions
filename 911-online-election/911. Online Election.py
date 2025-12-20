class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leading = [] #[time, leading]
        leader = persons[0]
        freqs = defaultdict(int)
    
        maxF = 0
        for i in range(len(persons)):
            time = times[i]
            person = persons[i]

            freqs[person] += 1

            if freqs[person] >= maxF:
                maxF = freqs[person]
                leader = person
            
            self.leading.append([time, leader])
    

                
    def q(self, t: int) -> int:
        #time <= t
        l = 0
        r = len(self.leading) - 1
        ans = None
        while l <= r:
            mid = (l + r) // 2

            if self.leading[mid][0] == t:
                return self.leading[mid][1]
            elif self.leading[mid][0] < t:
                ans = self.leading[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
class TweetCounts:

    def __init__(self):
        self.tweets = {} #user : tweets []
        self.seconds = {"minute": 60,
                        "hour": 3600,
                        "day": 86400,            
                        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = [time]
            return
        self.tweets[tweetName].append(time)
        

        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        seconds = self.seconds[freq]

        ans = [0] * (((endTime - startTime) // seconds) + 1)
        
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                ans[(t - startTime) // seconds] += 1
        
        return ans



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
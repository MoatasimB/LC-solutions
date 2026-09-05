class Twitter:

    def __init__(self):
        self.dic = defaultdict(set)
        self.stream = deque()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stream.appendleft((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []

        for uId, tweet in self.stream:
            if uId == userId or uId in self.dic[userId]:
                ans.append(tweet)
                if len(ans) == 10:
                    break
        
        return ans
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.dic[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.dic[followerId]:
            self.dic[followerId].remove(followeeId)
        

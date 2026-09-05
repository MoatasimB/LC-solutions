class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) #user: [tweets, time]
        self.follows = defaultdict(set) #user: {follows}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.time])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        posts = [] #maxHeap
        self.follows[userId].add(userId)
        for person in self.follows[userId]:
            person_posts = self.tweets[person]
            idx = len(self.tweets[person]) - 1
            if idx < 0:
                continue
            last_id, time = person_posts[idx]
            heapq.heappush(posts, [-time, last_id, idx, person])
        
        while posts and len(feed) < 10:
            _, last_id, idx, person = heapq.heappop(posts)
            feed.append(last_id)
            person_posts = self.tweets[person]
            idx -=  1
            if idx < 0:
                continue
            last_id, time = person_posts[idx]            
            heapq.heappush(posts, [-time, last_id, idx, person])

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
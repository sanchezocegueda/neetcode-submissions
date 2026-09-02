import heapq

class TwitterUser:

    def __init__(self, userId: int):
        self.userId = userId
        self.tweets = []
        self.followers = set()
        self.followed = set()

class Twitter:

    def __init__(self):
        self.users: dict[int, TwitterUser] = {}
        self.timestamp = 0 # monotonically decreasing with each tweet (neg bc minheap)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # O(1) operation:
        tweet = (self.timestamp, userId, tweetId)
        self.timestamp -= 1

        # Add tweet to personal collection of tweets
        if userId not in self.users:
            self.users[userId] = TwitterUser(userId)

        user = self.users[userId]
        
        user.tweets.append(tweet)

        

    def getNewsFeed(self, userId: int) -> List[int]:
        # generate feed on the fly
        feed = []
        if userId not in self.users:
            self.users[userId] = TwitterUser(userId)
        user = self.users[userId]
        n = min(10, len(user.tweets))
        for tweet in user.tweets[-n:]:
            heapq.heappush(feed, tweet)
        
        for followee in user.followed:
            n = min(10, len(followee.tweets))
            for tweet in followee.tweets[-n:]:
                heapq.heappush(feed, tweet)

        n = min(10, len(feed))

        ret = []
        for _ in range(n):
            ret.append(heapq.heappop(feed)[2])


        return ret

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.users:
            self.users[followerId] = TwitterUser(followerId)
        follower = self.users[followerId]

        if followeeId not in self.users:
            self.users[followeeId] = TwitterUser(followeeId)
        followee = self.users[followeeId]
        
        follower.followed.add(followee)
        followee.followers.add(follower)
    

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.users:
            self.users[followerId] = TwitterUser(followerId)
        follower = self.users[followerId]

        if followeeId not in self.users:
            self.users[followeeId] = TwitterUser(followeeId)
        followee = self.users[followeeId]

        if follower in followee.followers:
            followee.followers.remove(follower)
        
        if followee in follower.followed:
            follower.followed.remove(followee)
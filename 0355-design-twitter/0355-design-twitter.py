import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.userFollow = defaultdict(set)
        self.userTweet = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        self.userTweet[userId].append((-self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.userFollow[userId].add(userId)
        res = []
        arr = []
        
        for id in self.userFollow[userId]:
            for tweet in self.userTweet[id]:
                heapq.heappush(arr, tweet)
                if len(arr) > 10:
                    heapq.heappop(arr)

        while arr:
            tweet = heapq.heappop(arr)[1]
            res.append(tweet)
            
        return res[::-1]  # Return tweets in reverse order for most recent first

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.userFollow[followerId] and followerId != followeeId:
            self.userFollow[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

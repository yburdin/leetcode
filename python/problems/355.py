from common import *


class Twitter:
    # Implement the Twitter class
    def __init__(self):
        # Initializes your twitter object.
        self.users = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Composes a new tweet with ID tweetId by the user userId.
        # Each call to this function will be made with a unique tweetId.
        self.tweets.append({'user_id': userId, 'tweet_id': tweetId})

        if userId not in self.users:
            self.users[userId] = {'follow': []}

    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieves the 10 most recent tweet IDs in the user's news feed.
        # Each item in the news feed must be posted by users who the user followed or by the user themself.
        # Tweets must be ordered from most recent to least recent.

        news_feed = []
        if userId in self.users:
            user_ids = self.users[userId]['follow'] + [userId]

            for tweet in self.tweets[::-1]:
                if tweet['user_id'] in user_ids:
                    news_feed.append(tweet['tweet_id'])

                    if len(news_feed) == 10:
                        return news_feed

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # The user with ID followerId started following the user with ID followeeId.
        if followeeId not in self.users:
            self.users[followeeId] = {'follow': []}

        if followerId not in self.users:
            self.users[followerId] = {'follow': []}

        if followerId in self.users and followeeId in self.users:
            self.users[followerId]['follow'].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # The user with ID followerId started unfollowing the user with ID followeeId.
        if followerId in self.users and followeeId in self.users[followerId]['follow']:
            self.users[followerId]['follow'].remove(followeeId)


class TestTwitter(unittest.TestCase):
    def test_355(self):
        with self.subTest('Example 1'):
            twitter = Twitter()

            # User 1 posts a new tweet (id = 5).
            twitter.postTweet(1, 5)

            # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
            twitter.getNewsFeed(1)

            # User 1 follows user 2.
            twitter.follow(1, 2)

            # User 2 posts a new tweet (id = 6).
            twitter.postTweet(2, 6)

            # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
            # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
            self.assertEqual(twitter.getNewsFeed(1), [6, 5])

            # User 1 unfollows user 2.
            twitter.unfollow(1, 2)

            # User 1's news feed should return a list with 1 tweet id -> [5],
            # since user 1 is no longer following user 2.
            self.assertEqual(twitter.getNewsFeed(1), [5])


if __name__ == '__main__':
    unittest.main()

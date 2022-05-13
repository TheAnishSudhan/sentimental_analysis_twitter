import tweepy

class SA:

   def __init__(self):
      self.tweets=None
      self.tweet_text=[]


   def download_data(self):
      consumer_key="VZkOM477t2QIQG0PdBcUZSQ1I"
      consumer_secret="U8Y1OtWA2NXgrMN1WjpbvIcPpfdbnj8jyT7NIeYi040SyocXLg"
      access_token="1525033970756632576-4IGmN9yyYhsVlJ2tyKF9pRqkIO9kCD"
      access_token_secret="IDidLDNG5obvDo5o960vnoH8xopPsH7wAZu6dPvtFj2lt"


      auth = tweepy.OAuth1UserHandler(
         consumer_key, consumer_secret, access_token, access_token_secret
      )

      api = tweepy.API(auth)

      keyword=input("Enter Keyword: ")
      tweet_count=int(input("Enter Number of tweets you want to analyse: "))

      self.tweets=api.search_tweets(q=keyword,count=tweet_count)

      for tweet in self.tweets:
         self.tweet_text.append(tweet.text)

      # public_tweets = api.home_timeline()
      # for tweet in public_tweets:
      #    print(tweet.text)

tweet_test=SA()
tweet_test.download_data()
for tweet in tweet_test.tweets:
      print(tweet.text)

#print(tweet_test.tweet_text)


from os import access
import tweepy
import csv

consumer_key = "iTCl8h8naW7VUXKe39aQJGFHk"
consumer_secret = "vu7Vdezstmj225ilsfuvtiYWcugnJxPD20DyE0MWvXpmRuAG3H-ge"
access_token = "1482518389599784960-K4N8au64RLXzSjrXgugaOMJkxJ2YPH"
access_token_secret = "fSmCh4k9d1HiibwSHIh6jIyCNBEm5TfnL3qFlR2S5qeR8"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id='realDonaldTrump', tweet_mode="extended").items(3)
for i in cursor:
    print(i)

public_tweets = api.home_timeline()
print(public_tweets[0])

# with open('tweets.csv', 'w') as file:
#     WORD = 'bitcoin'
#     w = csv.writer(file)
#     w.writerow(['timestamp', 'tweet_text'])

#     # for tweet in tweepy.Cursor(api.search_tweets(), q=WORD + ' -filter:retweets',
#     #                                lang="en", tweet_mode='extended').items(100):
#     #         w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8')])
#     cursor = tweepy.Cursor(api.search_tweets, q="Bitcon -filter:retweets", tweet_mode="extended").items(1)
#     for i in cursor:
#         print(i.full_text)
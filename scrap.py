import tweepy
from tweepy import OAuthHandler
import pandas as pd

# """I like to have my python script print a message at the beginning. This helps me confirm whether everything is set up correctly. And it's nice to get an uplifting message ;)."""

print("You got this!")

access_token = '1482518389599784960-K4N8au64RLXzSjrXgugaOMJkxJ2YPH'
access_token_secret = 'fSmCh4k9d1HiibwSHIh6jIyCNBEm5TfnL3qFlR2S5qeR8'
consumer_key = 'iTCl8h8naW7VUXKe39aQJGFHk'
consumer_secret = 'vu7Vdezstmj225ilsfuvtiYWcugnJxPD20DyE0MWvXpmRuAG3H-ge'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []

count = 1

for tweet in tweepy.Cursor(api.search, q="@BNonnecke", count=450, since='2020-02-28').items(50000):
	
	print(count)
	count += 1

	try: 
		data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
		data = tuple(data)
		tweets.append(data)

	except tweepy.TweepError as e:
		print(e.reason)
		continue

	except StopIteration:
		break

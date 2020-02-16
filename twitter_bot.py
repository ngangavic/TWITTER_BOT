import tweepy
import time

auth= tweepy.OAuthHandler('02L1UDWXMRncxVjTdamNGZYcv','gPBMLZDCgsNMJIJLOMJDbxQ1Jy347y8d92fd1wg8UOWXDKSkKE')
auth.set_access_token('1139186989733990401-GaJwlWSeampD30HQtHeczem4dSHxFwkey','y6xYvxk7fFMvGBYyzy4kDI3KVJKbKjk5UPOJPuP019y8C')

api=tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
#print(user)
#this prints all my twitter details

#shows the list of all my twitter followers

#for follower in tweepy.Cursor(api.followers).items():
 #   print(follower.name

 
search='#100DaysOfCode'# e.g @freeCodeCamp
number_of_tweets = 20
for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
     try:
         print('Tweet Liked')
         tweet.favorite()
         print('Retweeted')
         tweet.retweet()
         time.sleep(10)
     except tweepy.TweepError as e:
         print(e.reason)
     except StopIteration:
         break

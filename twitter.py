import json
import tweepy
import pandas as pd
from tweepy import OAuthHandler

def twitter(consumer_key, consumer_secret, access_token, access_secret, lat, long, r):

	try :

		#consumer_key = input("Enter consumer key: ")
		#consumer_key = text_input.get()
		#consumer_secret = input("Enter consumer secret: ")
		#access_token = input("Enter access token: ")
		#access_secret = input("Enter access token secret: ")

		#connect with twitter api
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_secret)

		api = tweepy.API(auth)
		user = api.get_user('2018Osint')

		#print ("Processing...")

	except tweepy.TweepError:
		raise SystemExit("Error. Failed to connect to Twitter.")

	#set up csv file format
	format = { "username":[], \
 		   "tweet":[], \
		   "time":[]}

	#lat = input("Enter latitude: ")
	#long = input("Enter longitude: ")
	#r = input("Enter search radius in km: ")
	geo = "{},{},{}km".format(lat, long, r)

	geo_tweets = [status for status in tweepy.Cursor(api.search, geocode=geo).items(100)]
	for item in geo_tweets:
		format["username"].append(item.user.name)
#		if 'retweeted_status' in dir(item):
#			tweet=item.retweeted_status.full_text
#		else:
#			tweet=item.full_text
		format["tweet"].append(item.text)
		format["time"].append(item.created_at)
		#Can print other information and format or write to file as needed

	format = pd.DataFrame(format)
	format.to_csv('twitterdata.csv')

#twitter()
#added for testing

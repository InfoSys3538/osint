## will hopefully scrape reddit for information

#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

##connect to reddit and store in variable 'reddit'
reddit = praw.Reddit(client_id='e3Vgbf0tP4TLGg', \
                     client_secret='_Sy6Ybkvmgp94LekrcvT1U0EBwg', \
                     user_agent='infosec project', \
                     username='dtlz89', \
                     password='sniperdude1499')

##accessing subreddit and storing it in 'subreddit' variable
subreddit = reddit.subreddit('aww')

##creates a list of the top 50 posts in the subreddit
top_subreddit = subreddit.top(limit=50)

##specifies which parts of post to capture
topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "body":[]}

##pulls information from each post
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["body"].append(submission.selftext)

##pandas makes this look nicer 
topics_data = pd.DataFrame(topics_dict)

##creating csv
topics_data.to_csv('redditdata.csv')
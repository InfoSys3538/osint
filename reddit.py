## will hopefully scrape reddit for information

#! usr/bin/env python3
import praw
import pandas as pd

def reddit_osint():
    ##connect to reddit and store in variable 'reddit'
    reddit = praw.Reddit(client_id='e3Vgbf0tP4TLGg', \
                         client_secret='_Sy6Ybkvmgp94LekrcvT1U0EBwg', \
                         user_agent='infosec project', \
                         username='dtlz89', \
                         password='sniperdude1499')

    ##accessing subreddit entered by user and storing it in 'subreddit'
    userinput = input('Enter the subreddit to scrape:')
    subreddit = reddit.subreddit(userinput)

    ##creates a list of the top posts in the subreddit
    top_subreddit = subreddit.top(limit=50)

    ##specifies which parts of post to capture
    topics_dict = { "id":[], \
                    "title":[], \
                    "body":[]}

    ##checks information from each post against word or phrase in 'wordcheck'
    for submission in top_subreddit:
        wordcheck = [".onion"]
        if any(x in (submission.selftext or submission.title) for x in wordcheck):
            topics_dict["title"].append(submission.title)
            topics_dict["id"].append(submission.id)
            topics_dict["body"].append(submission.selftext)

    print("Scraping top 200 posts in r/" + userinput + " for: " + " ".join(map(str, wordcheck)))

    ##pandas makes this look nicer 
    topics_data = pd.DataFrame(topics_dict)

    ##creating csv and creating new filename if one already exists
    topics_data.to_csv("redditdata-" + userinput + ".csv")
    print('Created CSV file')
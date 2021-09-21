# ctrl+ alt+ n  to run the ptthon code and see the output 

#https://praw.readthedocs.io/en/stable/

import praw
# import random

reddit = praw.Reddit(
    client_id="oVGuO9-eIG-jtJ_kMjb5Sg",
    client_secret="2in5x6jBkHGR-0NVZDhDbBxU7-Jisw",
    user_agent="<console:Banana:1.0>",
    username="banan_bot",
    password="lumia535"
)

subreddit = reddit.subreddit("television")
sad_quotes = ["“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.”","“So many books, so little time.”"]
for submission in subreddit.hot(limit=10):
    # print("-------------")
    # print(submission.title)
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " fuck " in comment_lower:
                print("***********")
                print(comment.body)
                print("***********")
               
                # random_index = random.randint(0,len(sad_quotes)-1)
                comment.reply('I m sorry, I was programmed a Bot to respond to all comments that contain fuck')
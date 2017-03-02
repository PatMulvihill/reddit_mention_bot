import praw
import config
import time
import os
import json

def bot_login():
    # r is the instance of reddit
    print("Attempting to log in...")
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "Pulverize's mention responder v0.1")
    print("Successfully logged in.")
    return r

def run_bot(r, comments_replied_to):
    lim = 100
    print("Obtaining %d most recent comments..." % (lim))

    for comment in r.subreddit('test').comments(limit=lim):
        searched_user = "/u/" + config.searched_username

        if searched_user in comment.body and comment.id not in comments_replied_to: #and comment.author != r.user.me():
            print("String with " + searched_user + " found in comment " + comment.id + ".")
            commenter_name = comment.author
            sub_name = comment.submission


            pm_string = "/u/" + str(commenter_name) + " has mentioned you in a [comment](https://www.reddit.com/" + str(sub_name) + ").\n\n>" + comment.body
            r.redditor(config.searched_username).message('You have been mentioned in a comment!', pm_string)
            print("Sent PM to " + searched_user + " because of comment " + comment.id)
            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Sleeping for 10 seconds...")
    # sleep for 10 seconds
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)
while True:
    run_bot(r, comments_replied_to)

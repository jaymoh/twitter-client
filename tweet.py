import sys

from functions import create_client, post_tweet

"""
This script posts a tweet to Twitter using the Tweepy library.
The tweet message is passed as a command-line argument.
Usage: python tweet.py 'Your tweet message here'

"""
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tweet.py 'Your tweet message here'")
        sys.exit(1)

    tweet_message = sys.argv[1]
    client = create_client()
    post_tweet(client, tweet_message)

import sys

from functions import create_client, post_tweet, prepare_tweet_open_ai

if __name__ == "__main__":
    twitter_client = create_client()
    # optional prompt
    if len(sys.argv) > 1:
        tweet_message = prepare_tweet_open_ai(prompt=sys.argv[1])
    else:
        tweet_message = prepare_tweet_open_ai()

    if tweet_message:
        post_tweet(twitter_client, tweet_message)

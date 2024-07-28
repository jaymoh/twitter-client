from openai import OpenAI
import tweepy
import sys
from dotenv import load_dotenv
import os
import random

"""
This function creates a Tweepy client object (V2 API) using the environment variables.
Returns:
    tweepy.Client: A Tweepy client object
"""


def create_client():
    # Load environment variables from .env file
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_key_secret = os.getenv("API_KEY_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    if not all([api_key, api_key_secret, access_token, access_token_secret]):
        print("Missing environment variables")
        sys.exit(1)

    return tweepy.Client(consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token,
                         access_token_secret=access_token_secret)


"""
This function creates a Tweepy API object (Standard V1.1 API) using the environment variables.
Returns:
    tweepy.API: A Tweepy API object
"""


def create_api():
    # Load environment variables from .env file
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_key_secret = os.getenv("API_KEY_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Authenticate to Twitter
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication:", e)
        sys.exit(1)

    return api


"""
This function posts a tweet to Twitter using the Tweepy library. (V2 API)
Parameters:
    twitter_client (tweepy.Client): A Tweepy client object
    message (str): The tweet message
"""


def post_tweet(twitter_client, message):
    try:
        twitter_client.create_tweet(text=message)
        print("Tweet posted successfully")
    except Exception as e:
        print("Error while posting tweet:", e)


"""
This function prepares a tweet using the OpenAI API.
Returns:
    str: The tweet message
"""


def prepare_tweet_open_ai(hashtag="#RutoMustGo", prompt=None):
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        print("Missing OpenAI API Key")
        sys.exit(1)

    # Generate a random tweet from unpopular dictators in history
    prompts = [
        "Give me a quote from an unpopular politician in history.",
        "Provide a historical quote from a notorious politicians.",
        "What's a quote from a leader that's not well-known?",
        "Tell me a quote from a fictional movie character who was a dictator. Without explaining about the movie.",
        "Provide a historical quote from a well-known political figure who was controversial.",
        "Give me a quote from a historical figure known for their controversial leadership.",
        "Share a quote from a historical leader who was widely criticized."
    ]

    # If a prompt is not provided, select a random prompt
    if not prompt:
        prompt = random.choice(prompts)

    client = OpenAI(api_key=openai_api_key)

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
                                                  messages=[
                                                      {"role": "system", "content": "You are a helpful assistant."},
                                                      {"role": "user", "content": prompt}
                                                  ])
        quote = response.choices[0].message.content.strip()
        print(quote)  # Uncomment to see the generated quote
        if len(quote) > 265:
            quote = quote[:262] + "..."
        return quote + " " + hashtag
    except Exception as e:
        print("Error while fetching quote:", e)
        return None

# todo: implement prepare_tweet_gemini_ai
#def prepare_tweet_gemini_ai(hashtag="#RutoMustGo", prompt=None):


"""
This function gets the trending topics for a specific location using the Tweepy library. (Standard V1.1 API)
The location is specified using the WOEID (Where On Earth IDentifier).
You can find WOEID values for different locations here:
https://gist.github.com/tedyblood/5bb5a9f78314cc1f478b3dd7cde790b9
Parameters:
    api (tweepy.API): A Tweepy API object
    woeid (int): The WOEID for the location
"""


def get_trends(api, woeid):
    try:
        trends = api.get_place_trends(id=woeid)
        with open(f'{woeid}_current_trends.txt', 'w') as f:
            for trend in trends[0]['trends']:
                f.write(trend['name'] + '\n')
    except Exception as e:
        print("Error while getting trends:", e)


"""
This function gets the tweets for a specific user using the Tweepy library. (V2 API)
Parameters:
    client (tweepy.Client): A Tweepy client object
    username (str): The Twitter username
    count (int): The number of tweets to retrieve (default is 10)
"""


def get_tweets(client, username, user_id, count=10, start_time=None, end_time=None):
    try:
        tweets = client.get_users_tweets(id=user_id, max_results=count, start_time=start_time, end_time=end_time)
        with open(f'{username}.txt', 'w') as f:
            for tweet in tweets.data:
                f.write(tweet.text + '\n')
    except Exception as e:
        print("Error while getting tweets:", e)


def get_user_data(client, username):
    try:
        user = client.get_user(username=username)
        return user
    except Exception as e:
        print("Error while getting user info:", e)

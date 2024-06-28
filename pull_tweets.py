from functions import create_client, get_tweets

if __name__ == "__main__":

    user_id = 458680528
    username = "hackinRoms"
    start_time = "2015-03-01T00:00:00Z"
    end_time = "2016-03-31T23:59:59Z"

    client = create_client()
    get_tweets(client=client, username=username, user_id=user_id, count=10, start_time=start_time, end_time=end_time)
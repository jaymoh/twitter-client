## INSPIRED BY RAGE

This repo has random scripts that I have created, so I can continuously tweet **#RutoMustGo** straight from my terminal.
It can also use OpenAI's GPT-3 to get random quotes and tweet them.

### Steps
1. Clone the repository.
2. Install Python and pip.
3. Install the dependencies using `pip install -r requirements.txt`
4. Create a Twitter Developer account and get your API keys from [here](https://developer.twitter.com/en/apps).
5. Create OpenAI account and get your API key from [here](https://platform.openai.com/api-keys).
6. Create an environment variable file `.env` and add your API keys to it. <br/> For example:
    ```
    API_KEY=<your twitter api key>
    API_KEY_SECRET=<your twitter api secret>
    ACCESS_TOKEN=<your twitter access token>
    ACCESS_TOKEN_SECRET=<your twitter access token secret>
    OAUTH2_CLIENT_ID=<your twitter oauth2 client id>
    OAUTH2_CLIENT_SECRET=<your twitter oauth2 client secret>
    OPENAI_API_KEY=<your openai api key>
    ``
7. To post a tweet from the terminal, run `tweet.py` with your tweet as the argument. <br/> For example: `python tweet.py "What a terrible regim!"` will post a tweet with the text "What a terrible regim!".
8. To get a random quote from OpenAI's GPT-3, run `random_quote_tweet.py` with your query as the argument. <br/> For example: `python random_quote_tweet.py "What is the meaning of life?"` will give you some answer based on the GPT-3 model.
9. If you don't want to provide a query, you can run `random_quote_tweet.py` without any arguments. <br/> For example: `python random_quote_tweet.py` will give you a random quote from an unpopular dictator in history using the GPT-3 model.
10. The free tier of Twitter API allows you to make 50 requests per day. <br/> You can set up a cron job to run the script every 30 minutes to get the most out of the free tier. <br/> For example: `*/30 * * * * /usr/bin/python3 /path/to/random_quote_tweet.py` will run the script every 30 minutes.
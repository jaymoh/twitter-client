from functions import get_trends, create_api

"""
This script gets the trending topics for a specific location using the Tweepy library.
The location is specified using the WOEID (Where On Earth IDentifier).
You can find WOEID values for different locations here: 
https://gist.github.com/tedyblood/5bb5a9f78314cc1f478b3dd7cde790b9
"""

if __name__ == "__main__":
    # WOEID for Worldwide is 1, for Kenya is 1528335, you can change this to any other WOEID for different locations
    WOEID = 1528335

    api = create_api()
    get_trends(api, WOEID)

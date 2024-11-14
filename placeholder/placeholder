import tweepy
import requests
import time

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def fetch_wembanyama_stats():
    # Fetch stats from a sports API
    # This is a placeholder URL; replace it with the actual API endpoint
    response = requests.get('https://api.sportsdata.io/v4/nba/scores/json/Players')
    data = response.json()
    # Find Wembanyama's stats
    for player in data:
        if player['Name'] == 'Victor Wembanyama':
            return player['Points']  # Assuming 'Points' is the key for points scored
    return 0

def check_and_tweet():
    points = fetch_wembanyama_stats()
    if points >= 90:  # Check if points are close to 100
        api.update_status(f"🚨 Warning: Victor Wembanyama has scored {points} points! He is close to breaking Wilt Chamberlain's 100-point record! 🚨")

# Main loop
while True:
    check_and_tweet()
    time.sleep(3600)  # Check every hour

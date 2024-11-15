import tweepy
import requests
import time
from nba_stats import fetch_player_stats

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def check_and_tweet(points):
    if points >= 90:  # Check if points are close to 100
        api.update_status(f"🚨 Warning: Victor Wembanyama has scored {points} points! He is close to breaking Wilt Chamberlain's 100-point record! 🚨")

# Main loop
while True:
    points = fetch_player_stats('Victor Wembanyama')  # Fetch points for Wembanyama
    check_and_tweet(points)  # Pass points to the check_and_tweet function
    time.sleep(3600)  # Check every hour

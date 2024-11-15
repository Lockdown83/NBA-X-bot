import requests

def fetch_player_stats(player_name):
    # Fetch stats from a sports API
    response = requests.get('https://api.sportsdata.io/v4/nba/scores/json/Players')
    data = response.json()
    
    # Find the player's stats
    for player in data:
        if player['Name'] == player_name:
            return player['Points']  # Assuming 'Points' is the key for points scored
    return 0

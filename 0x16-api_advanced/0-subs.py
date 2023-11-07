#!/usr/bin/python3
"""
0-subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "MyRedditBot/1.0"  # Set a custom User-Agent to avoid Too Many Requests error
    }
    
    try:
        response = requests.get(url, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            return response_data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print(subscribers)

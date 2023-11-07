#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints
    the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, it prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        # Set a custom User-Agent to avoid Too Many Requests error
        "User-Agent": "MyRedditBot/1.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            for post in response_data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

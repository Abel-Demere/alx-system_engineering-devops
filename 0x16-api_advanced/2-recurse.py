#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    If the subreddit is invalid, it returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyRedditBot/1.0"  # Set a custom User-Agent to avoid Too Many Requests error
    }
    params = {
        "limit": 100,  # Number of posts per request (maximum is 100)
        "after": after  # Use 'after' to paginate through the results
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()
        if response.status_code == 200:
            for post in response_data['data']['children']:
                hot_list.append(post['data']['title'])
            after = response_data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)  # Recursively fetch more posts
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

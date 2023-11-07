#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses titles, and prints a sorted count of given keywords.
    """
    if count_dict is None:
        count_dict = {}
    
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
                title = post['data']['title'].lower()
                for word in word_list:
                    if f" {word} " in f" {title} ":
                        if word in count_dict:
                            count_dict[word] += 1
                        else:
                            count_dict[word] = 1
            after = response_data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                for keyword, count in sorted_counts:
                    print(f"{keyword}: {count}")
        else:
            return None
    except Exception as e:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Example: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        result = count_words(subreddit, word_list)
        if result is None:
            print("No posts match or the subreddit is invalid.")

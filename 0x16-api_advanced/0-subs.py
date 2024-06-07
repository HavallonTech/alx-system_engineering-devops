#!/usr/bin/python3
"""
Script that query sub on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Kestercode'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    else:
        subredit_data = response.json().get('data')
        return subredit_data.get('subscribers')

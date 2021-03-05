"""
Script to publish tweets from a source text file.
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import datetime
import random
import tweepy


def open_note(source_file, tweets_file):
    """
    Use this function to import a new tweet from the source text file.

    Params:
    Source File: Path to the text file.
    Tweets: Path to the text file containing the Tweets already published.

    Returns a new tweet.
    """
    random.seed(datetime.now())
    with open(source_file, 'r', encoding='utf8') as source:
        source_list = source.readlines()
        tweets = open(tweets_file, 'r', encoding='utf8')
        tweets_list = tweets.readlines()
        if len(source_list) == len(tweets_list):
            tweets_list = []
            tweets = open(tweets_file, 'w', encoding='utf8')
        tweets.close()
        new_tweet = choose_text(source_list, tweets_list)
        with open(tweets_file, 'a', encoding='utf8') as tweets:
            tweets.write(note)
    new_tweet = new_tweet.replace('\n', '').replace('|', '\n').strip()
    return new_tweet


def choose_text(source_list, tweets_list):
    """
    Use this function to randomly choose a new tweet from the source text file.

    Params:
    Source List: List with all possible tweets from source text file.

    Returns a randomly picked new tweet.
    """
    new_tweet = random.choice(source_list)
    if new_tweet in tweets_list:
        choose_text(source_list, tweets_list)
    else:
        return new_tweet


def post_tweet(note):
    """
    Use to tweet a new note from the book 'Notes on the cinematography'.

    Publishes a new tweet using the @robotbresson's Twitter's profile.
    If a note is longer than what Twitter supports for one single tweet,
    the script will divide the note and convert it into a Twitter's thread.
    """
    API_KEY = 'your API key number here'
    API_SECRET_KEY = 'your API secret number here'
    ACCESS_TOKEN = 'your access token here'
    ACCESS_TOKEN_SECRET = 'your access token secret here'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    twitter_API = tweepy.API(auth)
    if '$' not in note:
        twitter_API.update_status(note)
    else:
        thread = note.split('$')
        for t in thread:
            if t == thread[0]:
                tweet = twitter_API.update_status(status=t)
                previous_tweet = tweet
            else:
                tweet = twitter_API.update_status(status=t,
                in_reply_to_status_id=previous_tweet.id,
                auto_populate_reply_metadata=True)
                previous_tweet = tweet


if __name__ == '__main__':
    note = open_note('./source/source.txt',
                     './twitter/tweets.txt')
    post_tweet(note)

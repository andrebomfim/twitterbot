"""
Script to publish tweets from a source text file.
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import datetime
import random
import tweepy


def open_text(source_file, destination_file):
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
        tweets = open(destination_file, 'r', encoding='utf8')
        tweets_list = tweets.readlines()
        if len(source_list) == len(tweets_list):
            tweets_list = []
            tweets = open(destination_file, 'w', encoding='utf8')
        tweets.close()
        new_tweet = choose_text(source_list, tweets_list)
        with open(destination_file, 'a', encoding='utf8') as tweets:
            tweets.write(new_tweet)
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
    elif new_tweet == '':
        choose_text(source_list, tweets_list)
    else:
        return new_tweet


def post_tweet(new_tweet):
    """
    Use to tweet a new text from your source file.

    Publishes a new tweet using the desired Twitter's account.
    If a text is longer than what Twitter supports for one single tweet,
    the script will divide the text and convert it into a Twitter's thread.
    """
    API_KEY = 'your API key number here'
    API_SECRET_KEY = 'your API secret number here'
    ACCESS_TOKEN = 'your access token here'
    ACCESS_TOKEN_SECRET = 'your access token secret here'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    twitter_API = tweepy.API(auth)
    if '$' not in new_tweet:
        twitter_API.update_status(new_tweet)
    else:
        thread = new_tweet.split('$')
        for t in thread:
            if t == thread[0]:
                tweet = twitter_API.update_status(status=t)
                previous_tweet = tweet
            else:
                tweet = twitter_API.update_status(status=t,
                in_reply_to_status_id=previous_tweet.id,
                auto_populate_reply_metadata=True)
                previous_tweet = tweet


def twitter_bot(source_file, destination_file):
    """
    Use this function to run the script.

    Params:
    Source File: Path to source text file.
    Destination File: Path to destination text file.
    """
    new_tweet = open_text(source_file, destination_file)
    print(f'The new tweet is:\n{new_tweet}')
    post_tweet(new_tweet)
    print('Posted successfully!')


def test_twitter_bot():
    """
    Use this function to run a test.

    Params:
    Source Test File: Path to source test file.
    Destination Test File: Path to destination test file.

    The source test file contains only 4 possible tweets.
    The first and second one are single lines texts.
    The third one contains two lines.
    The fourth one creates a thread with a tweet and a comment.
    """
    SOURCE_TEST_FILE = './source/test_source.txt'
    DESTINATION_TEST_FILE = './destination/test_destination.txt'
    new_test_tweet = open_text(SOURCE_TEST_FILE,
                               DESTINATION_TEST_FILE)
    print(f'Testing...\nThe new tweet is:\n{new_test_tweet}')
    post_tweet(new_test_tweet)
    print('Posted successfully!')


if __name__ == '__main__':
    twitter_bot('./source/source.txt',
                './destination/destination.txt')

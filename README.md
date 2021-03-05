# twitterbot

Twitter bot for publishing text from a plain txt source file.

It randomly chooses one text line from a source text file and publishes it in your desired twitter account.

For enabling the account to be accessed by this script, as well as getting the API key, API Secret Key, Access Token and Access Token Secret, please visit the [Twitter API's documentation](https://developer.twitter.com/en/docs/twitter-api).

Requires [Tweepy Python Library](https://www.tweepy.org/).

Used originally in the [Robot Bresson](https://www.twitter.com/robotbresson) personal project. This bot posts, every day, one different note from Robert Bresson's _Notes on the Cinematographer_ book.

> Models automatically inspired, inventive. - Robert Bresson

Inspired by Twitter's bot [_Grande Sertão_](https://twitter.com/veredasbot).

## Contents

1. twitterbot.py
2. source folder and source.txt
3. destination folder and destination.txt
4. test folder and source and destination txt files for testing.
5. requirements.txt for deployment in a cloud service such as Heroku.
6. runtime.txt for deployment in a cloud service such as Heroku.

## About the Script, Source and Tweets (Destination) files.

The text you intend to publish on Twitter should be saved in the source.txt file. Each time your script is run, it randomly chooses one line of text from the source file and checks if it's been posted before. If not, it publishes on Twitter. If yes, it chooses another line of text.

If the all the lines from the source file have been published, the script erases the destination file and creates a new one in order to restart the process.

To begin your project, you should erase the contents from both the source and destination files. They were previously filled with some instructions, which should be observed as follows.

### Source file

1. Each line of the text file is a tweet. If you hit the Enter button and create a new line, it will be a new tweet.
2. If you want to split one tweet into many lines, use a `|` (vertical line). Don't create a new line for the same tweet, or it will become a new tweet.
3. If your content is longer than 280 characters, Twitter's standard for one tweet, the script will create a thread. I chose to manually indicate when to break the text using the `$` (dollar bill sign). You can have as many `$`s as you want.

### Destination file

1. This is the destination file for the tweets published in the desired account. Its purpose is to control what has been published.
2. You should see the same content copied from the source file, including the `|` and `$` from the previously formatted text.
3. Once your project has begun, don't modify the contents of this file, unless you want to give another chance to some text that has been posted before.
4. When this file matches the source file's number of lines, it is erased and recreated from scratch.

## Using the Script

In order to use the script, fill the source file with the desired content and replace these variables with the proper keys, which should be generated using [Twitter's API](https://developer.twitter.com/en/docs/twitter-api):

```python
API_KEY = 'your API key number here'
API_SECRET_KEY = 'your API secret number here'
ACCESS_TOKEN = 'your access token here'
ACCESS_TOKEN_SECRET = 'your access token secret here'
```

Once filled, simply run the script or import it and use the following function:

```python
twitter_bot('./source/source.txt', './destination/destination.txt')
```

If you don't have filled your source file yet, you can also run a test with four possible tweets.
1. Single line tweet.
2. Single line tweet.
3. Tweet with two lines.
4. Thread with a single line tweet and a single line comment.

In order to run the test, import the script and run the following function:

```python
test_twitter_bot()
```


Abraço,

**André Bomfim**

# Import Libraries
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import pandas as pd
import re
from textblob import TextBlob
import time
import tweepy

def get_authen():
    # Authentication
    apiKey = os.getenv('apiKey')
    apiSecret = os.getenv('apiSecret')
    accessToken = os.getenv('accessToken')
    accessTokenSecret = os.getenv('accessTokenSecret')
    auth = tweepy.OAuthHandler(apiKey, apiSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    return api

def get_keyword():
    keyword = input("Please enter keyword to search: ")
    return keyword

def get_numOfTweet():
    numOfTweet = input ("Please enter the number of tweets to analyze: ")
    return numOfTweet

def test_numOfTweet(numOfTweet):
    # number of input tweets should be an integer from 0 to 2000
    if numOfTweet.isdigit() and int(numOfTweet) <= 2000 and int(numOfTweet) >= 0:
        return numOfTweet
    else: 
        return "input_num_wrong"

def get_twi_list(keyword, numOfTweet):
    # search tweets
    api = get_authen()
    tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(int(numOfTweet))
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet.text)

    tweet_list = pd.DataFrame(tweet_list)
    # delete duplicates
    tweet_list.drop_duplicates(inplace = True)

    return tweet_list

def sentiment_analyze(tweet_list):
    #Extracting text values
    tw_list = pd.DataFrame(tweet_list)
    if tw_list.empty:
        return tw_list
    tw_list["text"] = tw_list[0]

    #Cleaning Text (RT, Punctuation etc)
    tw_list = pd.DataFrame(tweet_list)
    tw_list["text"] = tw_list[0]
    remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
    rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)
    tw_list["text"] = tw_list.text.map(remove_rt).map(rt)
    tw_list["text"] = tw_list.text.str.lower()

    if tw_list.empty:
        return tw_list

    #Calculating Negative, Positive, Neutral and Compound values
    tw_list[['polarity', 'subjectivity']] = tw_list['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in tw_list['text'].iteritems():
        score = SentimentIntensityAnalyzer().polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        if neg > pos:
            tw_list.loc[index, 'sentiment'] = "negative"
        elif pos > neg:
            tw_list.loc[index, 'sentiment'] = "positive"
        else:
            tw_list.loc[index, 'sentiment'] = "neutral"
        tw_list.loc[index, 'neg'] = neg
        tw_list.loc[index, 'neu'] = neu
        tw_list.loc[index, 'pos'] = pos
        tw_list.loc[index, 'compound'] = comp

    #Creating new data frames for all sentiments (positive, negative and neutral)
    tw_list_negative = tw_list[tw_list["sentiment"]=="negative"]
    tw_list_positive = tw_list[tw_list["sentiment"]=="positive"]
    tw_list_neutral = tw_list[tw_list["sentiment"]=="neutral"]

    return tw_list

def count_values_in_column(data):
    #Function for count_values_in single columns
    feature = "sentiment"
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

def search_limit_alert(time_diff, search_num):
    # stop searching when search 15 times in 15 minutes
    if time_diff/60 < 15 and search_num >= 15:
        return True
    else:
        return False

if __name__ == "__main__":
    # Instantiate an object
    start_time = time.time()
    search_num = 0

    while True:
        end_time = time.time()
        search_limit_alert(end_time - start_time, search_num)
        keyword = "red sox"
        numOfTweet = 2
        tweet_list = get_twi_list(keyword, numOfTweet)
        tw_list = sentiment_analyze(tweet_list)
        search_num = search_num + 1
        count_values_in_column(tw_list)

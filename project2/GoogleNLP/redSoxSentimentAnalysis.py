import tweepy
import re
from google.cloud import language
from google.cloud import language_v1
from nltk.tokenize import WordPunctTokenizer
import pandas as pd

# Authentication
apiKey = ""
apiSecret = ""
accessToken = "" 
accessTokenSecret = ""
auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Instantiates a client
client = language_v1.LanguageServiceClient()

#search tweets
keyword = input("Please enter keyword to search: ")
numOfTweet = int(input ("Please enter the number of tweets to analyze: "))

tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(numOfTweet)
tweet_list = []
for tweet in tweets:
    tweet_list.append(tweet.text)

tweet_list = pd.DataFrame(tweet_list)
print("search number: ",len(tweet_list))

# delete duplicates
tweet_list.drop_duplicates(inplace = True)
print("total number: ",len(tweet_list))

#Extracting text values
tw_list = pd.DataFrame(tweet_list)
tw_list["text"] = tw_list[0]
# print(tw_list.head(10))

#Cleaning Text (RT, Punctuation etc)
#Creating new dataframe and new features
tw_list = pd.DataFrame(tweet_list)
tw_list["text"] = tw_list[0]

#Removing RT, Punctuation etc
remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)
tw_list["text"] = tw_list.text.map(remove_rt).map(rt)
tw_list["text"] = tw_list.text.str.lower()
# print(tw_list.head(10))

# sentiment analysis
for index, tweet in tw_list['text'].iteritems():
    document = language_v1.Document(content=tweet.encode('utf-8'), type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    tw_list.loc[index, 'score'] = sentiment.score

    if sentiment.score >= -1.0 and sentiment.score < -0.25:
        tw_list.loc[index, 'sentiment'] = "negative"
    elif sentiment.score >= -0.25 and sentiment.score <= 0.25:
        tw_list.loc[index, 'sentiment'] = "neutral"
    else:
        tw_list.loc[index, 'sentiment'] = "positive"

print(tw_list.head(10))


#Creating new data frames for all sentiments (positive, negative and neutral)

tw_list_negative = tw_list[tw_list["sentiment"]=="negative"]
tw_list_positive = tw_list[tw_list["sentiment"]=="positive"]
tw_list_neutral = tw_list[tw_list["sentiment"]=="neutral"]

#Function for count_values_in single columns

def count_values_in_column(data,feature):
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

#Count_values for sentiment
print(count_values_in_column(tw_list,"sentiment"))

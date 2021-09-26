## Red sox Sentiment Analysis on Twitter
Jiawei Zhao, zhaojw@bu.edu  

The Boston Red Sox are an American professional baseball team based in Boston. I am going to use Python library - Tweepy - for accessing the Twitter API to analyse what people think about the performance of Red Sox recently.

### 1. Tweets Search
In order to search tweets related to "Red Sox", I set "Red Sox" as the keyword and want to get 1500 tweets to analyze.
![图片](https://user-images.githubusercontent.com/59852184/134815690-caa43254-689f-451e-8c77-955b74850c77.png)

By using api.search_tweets() function, I get 1500 tweets in tweet_list with keyword "red sox".

### 2. Data Preparation
I found there are lots of duplicated tweets as well as RT, link and some other unuseful characters in the list. For more accurate sentiment analysis, the tweet_list is cleaned by dropping duplications and removing RT, link, punctuation characters and finally convert to lowercase.
Finally, the list has 944 unique tweets and the text of tweets are extracted.

### 3. Sentiment Analysis
By calculating polarity, subjectivity, sentiment, negative, positive, neutral and compound parameters of the texts, I get a new feature of the list, sentiment.
Based on the sentiment parameter, the texts are seperated in three group which means negative list, positive list and neutral list respectively.
![图片](https://user-images.githubusercontent.com/59852184/134824896-7961811b-ad47-4adf-9550-95284eeae788.png)

Furthermore, we can find only 17.69% users who had negative comments on Rex Sox.

![图片](https://user-images.githubusercontent.com/59852184/134824926-4e45d4e8-faec-4f68-ac7b-8efd397efa37.png)

### 4. Discussion
In this report, 1500 tweets related to "Red Sox" are collected and finally 944 clean texts are extrated by pretreatment. Additionally, a new feature "Sentiment" is calculated by sentiment analysis. We find that most people have positive or neutral attitude on this team. 
Aside from mentioned above, we can also realize which words most used in these positive tweets and negative tweets.


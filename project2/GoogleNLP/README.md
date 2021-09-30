## Red sox Sentiment Analysis by Using Google NLP API
Jiawei Zhao, zhaojw@bu.edu  

In this report, I'm going to make Sentiment Analysis of tweets related to Red sox by Using Google NLP API.

### 1. Tweets Search and Data Preparation
We are going to use tweepy to gather the tweet data. And then the tweet list is cleaned by dropping duplications and removing RT, link, punctuation characters and finally convert to lowercase.
Code same as https://github.com/zhaojiawei86/ec601/tree/main/project2/TwitterAPIs.  
In this step, we collected 1500 original tweets, and finally get 1116 cleaned unique text.

### 2. Sentiment Analysis
In this report, I use Google Natural Language API to get a tweet’s sentiment. In Google’s Sentiment Analysis, sentiment score is the score of the sentiment ranges from -1.0 (very negative) to 1.0 (very positive).
Based on the sentiment parameter, the texts are labeled in negative, neutral or positive.
![image](https://user-images.githubusercontent.com/59852184/135372124-d947121f-e092-4f56-9093-c70c2269fa20.png)

Furthermore, we can find recently there are 31.27% users had negative comments on Rex Sox.

![image](https://user-images.githubusercontent.com/59852184/135372187-8d3480c9-665d-4d33-b401-b32fc31ef5fc.png)

### 3. Discussion
In this report, 1500 tweets related to "Red Sox" are collected and finally 1161 clean texts are extrated by pretreatment. Additionally, a new feature "Sentiment" is calculated by sentiment analysis. We find that about 1/3 of people have negative attitude on this team, which is higher than the result calculated by using twitter API tool. 
This report need a further research on why the percentage of negative comments are increased by using Google NLP API. 


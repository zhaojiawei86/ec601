## Red sox Sentiment Analysis by Using Google NLP API
Jiawei Zhao, zhaojw@bu.edu  

In this report, I'm going to make Sentiment Analysis of tweets related to Red sox by Using Google NLP API.

### 1. Tweets Search and Data Preparation
We are going to use tweepy to gather the tweet data. And then the tweet list is cleaned by dropping duplications and removing RT, link, punctuation characters and finally convert to lowercase.
Code same as https://github.com/zhaojiawei86/ec601/tree/main/project2/TwitterAPIs.  
In this step, we collected 500 original tweets, and finally get 157 cleaned unique text.
![图片](https://user-images.githubusercontent.com/59852184/139601088-c6aea73a-8113-48ca-ac81-70a9e380cf76.png)

### 2. Sentiment Analysis
In this report, I use Google Natural Language API to get a tweet’s sentiment. In Google’s Sentiment Analysis, sentiment score is the score of the sentiment ranges from -1.0 (very negative) to 1.0 (very positive).
Based on the sentiment parameter, the texts are labeled in negative, neutral or positive.
![图片](https://user-images.githubusercontent.com/59852184/139601121-232e390d-015c-4b20-a976-3dcc4a7d575e.png)

Furthermore, we can find recently there are about 70% users had non-negative comments on Rex Sox.

![图片](https://user-images.githubusercontent.com/59852184/139601132-c13196ca-9f6d-4b0f-a9ab-a866e69c92bb.png)

### 3. Discussion
In this report, 500 tweets related to "Red Sox" are collected and finally 157 texts are extrated by pretreatment. Additionally, a new feature "Sentiment" is calculated by sentiment analysis. We find that about 70% of people have non-negative attitude on this team, which is higher than the result calculated by using twitter API tool. 
This report need a further research on why the percentage of negative comments are increased by using Google NLP API. 


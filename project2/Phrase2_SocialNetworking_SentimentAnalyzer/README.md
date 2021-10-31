# Social Media Sentiment Analyzer
Jiawei Zhao  
zhaojw@bu.edu

In this report, I'm going to introduce a social media analyzer that could help people analyze the sentiment of specific keywords. In this way, people could find others' comments as well as attitude towards what they care about. This product is designed by using Twitter API.

## Users
This analyzer could be used by three groups of people:
1. Used by Product Manager or Data Analyzer in companies;
2. Used by students or researchers in university or scientific institution;
3. Used by the public who are interested in analyzing sentiment of daily products.

## User Stories
As a Data Analyzer or Product Manager,
1. When they publish a new version of application or function of their products, they will care about the users' using experiments. They hope to use the sentiment analyzer to find the feedback of their new product which could help them decide whether it is a useful function or just give it up.
2. A product Data Analyzer or Product Manager will also want to know more of their past products. The change of analyzer's result could help them to improve the existed products. 

As a student or researcher,
1. Want to learn more about sentiment analyzer, the best way is to familier with others' code first.
2. Already had a model of theirselves, and decided to improve their model, so they want to compare theirs with other products.

As the public,  
When a consumer wants to know more about a new product, just like iphone 13. They will use the analyzer to find the comments of other consumers, according to the analyze result, they will decide whether they could buy this new product.

## MVP
According to user stories, I find that the most important function of this analyzer is:
1. Could input the keyword as well as the number of tweets what the users want;
1. Could get the detail comments or attitude of specific keyword;
2. Could get the result of sentiment analyze, like the percentage of positive or negative sentiment;
3. Could get the change of attitude toward the same product periodly
4. Could supply open source code and dataset.

## Modular Design
This product is used for sentiment analyzing when users input keywords what they want. So the thing the users need to do is just pass the word they want to search in the input box. Finally, they will get the content of the related tweets, the sentiment points toward these text as well as the analyze result.
All the code information will be hided from the users.

## Introduction of Product
I will take the new function of Wechat application in China called "wechat status" as an example to introduce my product.
I set "wechat status" as the keyword and want to get 500 tweets to analyze.In this step, we collected 500 original tweets, and finally get 187 cleaned unique text.  
![图片](https://user-images.githubusercontent.com/59852184/139601639-a8214b2f-0482-4440-a4cf-81705654cca0.png)

By calculating polarity, subjectivity, sentiment, negative, positive, neutral and compound parameters of the texts, I get a new feature of the list, sentiment. Based on the sentiment parameter, the texts are seperated in three group which means negative list, positive list and neutral list respectively.
![图片](https://user-images.githubusercontent.com/59852184/139601666-1a70ed33-8d26-47e7-8ffa-ba2657bb5f82.png)![图片](https://user-images.githubusercontent.com/59852184/139601672-1466daf3-1849-40ea-b3e4-593c7dfe62a0.png)

Finally, we can find recently there are 9.09% (by using twitter API) users had negative comments on wechat status. 
![图片](https://user-images.githubusercontent.com/59852184/139601697-bab0a6a6-b84c-40c7-a269-a8ec40f80cdc.png)


## Testing
The program could also do some tests.
1. If there is 0 tweet found, the program will give a warning instead of program errors and stop the analyzing. This could help tell the users why analyzing is not worked.
2. If users input non-integer as the number of tweets or input a number too much, Twitter API will output errors too. Instead of disunderstanding program errors, my program will check the input, give a remind and pass the input until users give a correct form.
3. There is a request limitation for twitter API, 15 requests in 15 minutes. In order to remind users before they over searching, my program will calculate searching times in 15 minutes and give a remind to users.
![图片](https://user-images.githubusercontent.com/59852184/139601997-8d6f3534-f0a4-4578-806c-8304aa62cc80.png)


## Discussion
I choose Twitter API to do Sentiment analyzing because there are some tweets cannot be analyzed by Google NLP. These tweets are labeled as nah by google nlp. Also, sometimes Google NLP will give warnings like "Language ca is not supported", which will stop the analysis.
Wechat is a Chinese APP. Twitter API sentiment analyzer would be much useful because it could support more languages.
Further research is needed to evaluate and combine the result of both API.   

![图片](https://user-images.githubusercontent.com/59852184/139601759-69e811cb-1691-46f8-9489-5822007a7487.png)
![image](https://user-images.githubusercontent.com/59852184/137636237-99a5e5a3-2649-47e8-845e-005a94fdc159.png)  




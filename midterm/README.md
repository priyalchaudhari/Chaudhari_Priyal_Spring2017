
# MIDTERM ANALYSIS:

# Question 2 Analysis 1:

# Opinion mining (AKA sentimental Analysis)of newspaper Headlines(Positive and neative score) using NLTK

### Goal of this analysis was to find out the opinions about the headlines over the years and calculating total score for the month. 
- I have used Archive API data for this analysis 
- done the grapph for 1 year file monthwise for more than 3 year data it takes too much time 
## Algorithm used:

### Part 1:

- First Tokanize the headline using NLTK 
- pass those tokens to Pos_Tagger for tagging each word
- The result of this is passed to Lemmatize the word in wordnet corpus of NLTK 
- This will determine which words to keep togather if you consider 'Good to go' if you read it togather it means different thing and if you read it separately it means different thing. 
- Normalize each word using Stremmer i have used Porter Stemmer in my analysis  becoz that was giving me desired result 
- Each stemmed(normalized) word is sent to synset which will give you set of synonyms of that word 
###### pass all those to SentiWordNet method which will give you Positive and Negathive score of the word

### Part 2:
- Calculate the score for each headline by summing the score of each word of that headline 
- If the score n(negative) > P(positive) asiign the polarity -1 to headline 
- If the score P(positive) > n(negative) assign the porarity +1 to headline 
- If not assign 0 
###### sum of all positive score of month vp
######  sum of all negative socre of month vn 
### total score = vp - vn 

- This analysis can be done on day by day basis if you have daily data. I have done on months because i have monthly data. 
- Result on daily data will be more accurate than monthly. 

# result:
![q2a1](https://cloud.githubusercontent.com/assets/25044602/23641160/e4ee0cb6-02bf-11e7-9185-d8ebdb9d7bf3.PNG)

## conclusion
- If you compair the results with timeline the score differs like at 2011 near september and october the score is low because of 9/11 
- Also in january 2017 the score is low because of new president news and controversies. 
- Error calculation can be inplimented for future scope 

# Question 2 Analysis 2:

## Finding the article in sports section related to given 2 words using NLTK API used is Article search in sports section 
### Goal of this analysis is to find articles related to words provided like Hero and poor so i wanted to see which are the headlines who praised the heros in sports and which are the headline related to poor performance. 

- In this analysis I first retrived all the related words to given 2 words
- Given words are passed to synset() method in wordnet which will give me all the names synonyms of the word
- I a searched for those words in article headline and found results. 

# Result:



# Question 2 Analysis_3
## Analysis to determine the complexity of article based on news desk 
#### Goal of this analysis is to find out articles under which news_desk are more complex 
- first i extracted the news desk and paragrapth of each article 
- Find the unique words in each article and total words in each article 
- Take ratio unique words/ total words = complexity ratio 
- result of this file is stored in csv file in desired folder
### conclusion:
- Most of the articles zipfs law as they use words repitatively.  

# Question 1 Analysis 1:

### Topic 1 contains a lot of meeting related words, perhaps they are fromemails that were sent as meeting notices.
### Topic 2 while related to business seems to be more about the processrather than the content of the core business. It has a lot   of terms relevant to business legalities.

## Goal of this analysis is to determine the conversation between two convicted people Skilling J and Lay K 
- Reason for Analysis:
   As observed It is well known that Jerey Skilling and Kenneth Lay, then CEO and Chairman of Enron respec- tively at the time    of the scandal, were holding regular meeting with their top executives in order to pressure them into finding new ways to hide    Enron's debt. Since the scandal was only made known to the public in 2001, it could well be the case that this abnormal      rise in meetings was an indicator of Enron's executives trying to cover up their accounting fraud. Topic 2 on the other hand    has a general decrease throughout the years. Since Topic 2 contains words like "contract", "deal" and "agreement", this might    well be an indicator of dwindling business activity throughout the years. The huge decrease after2001 makes sense given    that it was only 8 months before the scandal.

#### Used NLTK to tokanize the mail body to get the related words

# Result
- In 1999:  {'topic_1': 235, 'topic_2': 86}
- in 2000:  {'topic_1': 5222, 'topic_2': 2024}
- in 2001:  {'topic_1': 6417, 'topic_2': 1857}

![q1a1](https://cloud.githubusercontent.com/assets/25044602/23640977/d73c76e4-02be-11e7-88b0-a066e83dc20b.PNG)


# Conclusion:
- As we can see there is significance increase in meeting related terms in 2001 compaired to 1999. And there is significant     decrease in business related terms in 2001. 

# Question 1 Analysis 2:
## Goal of this analysis is to find the employes and there most frequent contact through Emails:
- Reason: The reason i wanted to do this analysis is as Enron CEOs commited froud i wanted to see how many employes are in frequent contact with the. 
- So by determinng that we can determine the chatter between the organisation and see whos envolved in the suspicious activities. 
- As pattern observed there are lot of communication between high level employees when the scandal made public 

#### One interesting fact that there are lot og emails going from Vincent J. Kaminski as he was the one aware of the faul play and against it . For months before Enron's demise, Vincent J. Kaminski warned superiors that the off-the-books partnerships and side deals engineered by Mr. Fastow were unethical and could bring down the company.

## Also i have checked conversation between Jeff Skilling and kenneth Lay and they are among top 5 most contacted of each other 

# Result:

![q1a2](https://cloud.githubusercontent.com/assets/25044602/23641094/7d7755a6-02bf-11e7-8f56-39c387816e00.PNG)

![q1a2 1](https://cloud.githubusercontent.com/assets/25044602/23641110/9add028a-02bf-11e7-9a5e-e7f84b80f970.PNG)

# Question 1 Analysis 3:

## Goal of this analysis is to find out how many refund request or emails the CEO LAY-K who was the CEO at the time the scandal got public got . Who are the persons who send those request 

- Reason: I wanted to see if he has got any refund request and who sent those request and how much money they are claiming . 
- Interesting fact is all those refund request email has found in deleted items folder . 
### used NLTK to tokanize the subject line of the email 
## Result: 

![q3a3](https://cloud.githubusercontent.com/assets/25044602/23641227/41a13c30-02c0-11e7-8eb3-3e89c0046037.PNG)


### conclusion :
- The conclusion i made from this analysis is he didnt pay attention to those request or he dont want others to find out about it hence he deleted those emails from his inbox. 




```python

```

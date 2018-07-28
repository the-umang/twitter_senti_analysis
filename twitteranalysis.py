#twitter analysis
#app name senti_analysis_umang
# pip install from cmd tweepy, textblob and matplotlib

#importing the libraries
from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/ float(whole)

#importing the consumerKey from apps.twitter.com/senti_analysis_umang
consumerKey = "rGa886CmX0meenqXfP0RoYaSA"
consumerSecret = "a7qyOpmS7zJBJ8J4uuWeip4l64K9wEDcw18OiHJeAkPeAwk6b2"
accessToken = "703605520645517314-Uxk0pthCDxrbmrODOQHQZFtCPr0mrmm"
accessTokenSecret ="4kC6iTnyPC5k4tg1Udz9s7yPiOJuASvJ7oEOP4F1lMF9P"


#establishing the connection with the api
auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken , accessTokenSecret)
api = tweepy.API(auth)

#search keyword or hashtag and number of first tweets to search 
searchTerm = input("Enter keyword/hashtag to search about: ")
noofsearchTerms = int(input("enter how many tweets to analyze:"))

##
tweets = tweepy.Cursor(api.search , q=searchTerm,result_type="recent",include_entities=True,lang="en").items(noofsearchTerms)
#for positive sentiments
positive = 0
#for negative sentiments
negative = 0
#for neutral sentiments
neutral = 0
#for average polarity sentiments
polarity = 0 

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity+= analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0.00):
        neutral+=1

    elif(analysis.sentiment.polarity < 0.00):
        negative+=1

    elif(analysis.sentiment.polarity > 0.00):
        positive+=1


positive = percentage(positive , noofsearchTerms)
negative = percentage(negative , noofsearchTerms)
neutral = percentage(neutral,noofsearchTerms)

positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')

#print("positive response" + positive)
#print("negative response" + negative)
#print("neutral response" + neutral)

print("How people are reacting on " + searchTerm + " by analyzing " + str(noofsearchTerms) + " Tweets. ")

if(polarity<0):
    print("Negative")
elif(polarity>0):
    print("Positive")
elif(polarity==0):
    print("Neutral")

labels = ['Positive [' + str(positive)+ '%]' ,'Neutral [' + str(neutral) + '%]','Negative [' +str(negative) + '%]']
sizes = [positive , neutral , negative]
colors = ['yellowgreen','gold','red']
patches,texts = plt.pie(sizes,colors = colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noofsearchTerms) + ' Tweets. ')
plt.axis('equal')
plt.tight_layout()
plt.show()







    

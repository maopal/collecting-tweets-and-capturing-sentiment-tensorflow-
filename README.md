# bitcoin-price-prediction


## Using Twitter BTC price sentiment 

### Collecting Tweets (Tweepy)

*streaming_with_error.py* file collects tweets, number of likes on each tweet, number of retweets on each tweet and datetime of tweet.  

    twitterStream.filter(track=["Bitcoin", "Ethereum", "Tezos", "Stellar", "Cardano", "Neo", "Tron", "Quant", "DigiByte"])
Tweets containing these key words are collected, but these can be changed to anything you want.
      
    on_error(self, status)
 Error handling function: This function allows us to reconnect in 5 seconds automatically if connection drops (i.e. if  too many api calls).

### twitter feed downtimes 

Tweets were collected on personal laptop so it was difficult to keep laptop on for 3 months consistently therefore there will be gaps in the dataset recorded in *Recorded downtimes.docx* 

## Finding Labelled data for training
Labeled data with positive, negative and neutral sentiment assigned to BTC tweet: https://data.world/mercal/btc-tweets-sentiment

"cleaning tweets data.py" This file removes emojis, "@" symbols and URLs from tweets, ensurng useful and interpretable information is provided to the Neural Network. Duplicate tweets were removed aswell. 

The Neural Network that trained on just 2 classes (neutral and positive) were significantly more accurate than training on 3 classes (positive, neutral and negative), moreover negative sentiment made up less than 10% of tweets in the dataset. 

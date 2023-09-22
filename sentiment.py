# import sentiment analysis model from Vader Sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initialize sentiment analyser *outside* of function
analyzer = SentimentIntensityAnalyzer()

def getSentiment(text):
    return analyzer.polarity_scores(text)
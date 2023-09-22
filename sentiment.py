# import sentiment analysis model from Vader Sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initialize sentiment analyser *outside* of function
analyzer = SentimentIntensityAnalyzer()

def getSentiment(text: str) -> dict[str, float]:
    return analyzer.polarity_scores(text)
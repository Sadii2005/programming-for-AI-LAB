# Sentiment Analysis

from textblob import TextBlob

# input text
sentence = "I really like this product, it is amazing!"

# create object
analysis = TextBlob(sentence)

# output sentiment
print("Text:", sentence)
print("Polarity:", analysis.sentiment.polarity)
print("Subjectivity:", analysis.sentiment.subjectivity)

# classification
if analysis.sentiment.polarity > 0:
    print("Sentiment: Positive")
elif analysis.sentiment.polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
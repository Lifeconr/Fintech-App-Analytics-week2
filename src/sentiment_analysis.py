import pandas as pd
from transformers import pipeline
from textblob import TextBlob
import os

# Load pre-trained model
sentiment_analyzer_distilbert = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    return_all_scores=True
)

# Load cleaned data
input_path = 'clean_reviews.csv'
df = pd.read_csv(input_path)

# Function to get DistilBERT sentiment
def get_distilbert_sentiment(text):
    result = sentiment_analyzer_distilbert(text)[0]
    positive_score = next(s['score'] for s in result if s['label'] == 'POSITIVE')
    negative_score = next(s['score'] for s in result if s['label'] == 'NEGATIVE')
    label = 'positive' if positive_score > negative_score else 'negative' if negative_score > positive_score else 'neutral'
    score = max(positive_score, negative_score)
    return label, score

# Function to get TextBlob sentiment
def get_textblob_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    return 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral', abs(polarity)

# Apply sentiment analysis
df[['distilbert_label', 'distilbert_score']] = df['review'].apply(lambda x: pd.Series(get_distilbert_sentiment(x)))
df[['textblob_label', 'textblob_score']] = df['review'].apply(lambda x: pd.Series(get_textblob_sentiment(x)))

# Aggregate by bank and rating
sentiment_summary_distilbert = df.groupby(['bank', 'rating']).agg({'distilbert_score': 'mean'}).reset_index()
sentiment_summary_textblob = df.groupby(['bank', 'rating']).agg({'textblob_score': 'mean'}).reset_index()

# Save results
output_dir = 'data/processed/'
os.makedirs(output_dir, exist_ok=True)
df.to_csv(os.path.join(output_dir, 'sentiment_results.csv'), index=False)
sentiment_summary_distilbert.to_csv(os.path.join(output_dir, 'sentiment_summary_distilbert.csv'), index=False)
sentiment_summary_textblob.to_csv(os.path.join(output_dir, 'sentiment_summary_textblob.csv'), index=False)
print(f"Saved sentiment results to {os.path.join(output_dir, 'sentiment_results.csv')}")
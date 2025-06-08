import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import nltk
from nltk.corpus import stopwords

# Load spaCy model and NLTK stopwords
nlp = spacy.load("en_core_web_sm")
nltk_stopwords = set(stopwords.words('english'))

# Load sentiment data
input_path = 'data/processed/sentiment_results.csv'
df = pd.read_csv(input_path)

# Preprocessing function
def preprocess_text(text):
    doc = nlp(text.lower())
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha and token.text not in nltk_stopwords])

df['processed_review'] = df['review'].apply(preprocess_text)

# Keyword extraction with TF-IDF
vectorizer = TfidfVectorizer(max_features=50, ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(df['processed_review'])
keywords = vectorizer.get_feature_names_out()

# Define theme mapping based on keywords
theme_mapping = {
    'ui_experience': ['ui', 'interface', 'design', 'layout', 'experience'],
    'transaction_performance': ['slow', 'crash', 'loading', 'transfer', 'performance'],
    'account_access': ['login', 'error', 'account', 'access'],
    'customer_support': ['support', 'help', 'customer', 'service'],
    'feature_requests': ['fingerprint', 'feature', 'update', 'request']
}

def assign_themes(review):
    themes = []
    for theme, keywords_list in theme_mapping.items():
        if any(keyword in review.lower() for keyword in keywords_list):
            themes.append(theme)
    return ', '.join(themes) if themes else 'other'

df['themes'] = df['processed_review'].apply(assign_themes)

# Save results
output_path = os.path.join('data/processed/', 'thematic_results.csv')
df.to_csv(output_path, index=False)
print(f"Saved thematic results to {output_path}")

# Summary per bank
theme_summary = df.groupby('bank')['themes'].value_counts().unstack(fill_value=0)
theme_summary.to_csv(os.path.join('data/processed/', 'theme_summary.csv'))
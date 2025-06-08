from google_play_scraper import reviews
import pandas as pd
from tqdm import tqdm

app_ids = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}

all_reviews = []

for bank_name, app_id in app_ids.items():
    print(f"Scraping reviews for {bank_name}...")
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        count=500,  # scrape slightly more in case of duplicates
        filter_score_with=None
    )
    for review in tqdm(result):
        all_reviews.append({
            "bank": bank_name,
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"].strftime('%Y-%m-%d'),
            "source": "Google Play"
        })

# Save raw reviews
df = pd.DataFrame(all_reviews)
df.to_csv("raw_reviews.csv", index=False)

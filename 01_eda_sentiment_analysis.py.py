import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import warnings
warnings.filterwarnings('ignore')

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv('netflix_titles.csv')
print(f"✅ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ── Clean Data ─────────────────────────────────────────
df.fillna('Unknown', inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

print("\n📊 ANALYSIS 1 — Content Split")
print(df['type'].value_counts())

print("\n📊 ANALYSIS 2 — Top 10 Countries")
print(df[df['country'] != 'Unknown']['country'].value_counts().head(10))

print("\n📊 ANALYSIS 3 — Top 10 Ratings")
print(df['rating'].value_counts().head(10))

print("\n📊 ANALYSIS 4 — Content added per year")
print(df['year_added'].value_counts().sort_index().tail(10))

# ── Sentiment Analysis ─────────────────────────────────
print("\n🧠 ANALYSIS 5 — Sentiment Analysis on Descriptions")
df['sentiment_score'] = df['description'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)
df['sentiment_label'] = df['sentiment_score'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)
print(df.groupby(['type', 'sentiment_label']).size())

# ── Visualizations ─────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.patch.set_facecolor('#141414')
plt.suptitle('Netflix Content Analysis', color='#E50914', fontsize=20, fontweight='bold')

# Plot 1 — Content Split
colors = ['#E50914', '#831010']
df['type'].value_counts().plot(kind='bar', ax=axes[0,0], color=colors)
axes[0,0].set_title('Movies vs TV Shows', color='white')
axes[0,0].set_facecolor('#1E1E1E')
axes[0,0].tick_params(colors='white')

# Plot 2 — Top 10 Countries
top_countries = df[df['country'] != 'Unknown']['country'].value_counts().head(10)
top_countries.plot(kind='barh', ax=axes[0,1], color='#E50914')
axes[0,1].set_title('Top 10 Countries', color='white')
axes[0,1].set_facecolor('#1E1E1E')
axes[0,1].tick_params(colors='white')

# Plot 3 — Ratings
df['rating'].value_counts().head(8).plot(kind='bar', ax=axes[0,2], color='#E50914')
axes[0,2].set_title('Content Ratings', color='white')
axes[0,2].set_facecolor('#1E1E1E')
axes[0,2].tick_params(colors='white')

# Plot 4 — Content by Year
yearly = df['year_added'].value_counts().sort_index()
yearly.plot(kind='line', ax=axes[1,0], color='#E50914', linewidth=2)
axes[1,0].set_title('Content Added by Year', color='white')
axes[1,0].set_facecolor('#1E1E1E')
axes[1,0].tick_params(colors='white')

# Plot 5 — Sentiment Distribution
sentiment_counts = df['sentiment_label'].value_counts()
sentiment_counts.plot(kind='pie', ax=axes[1,1],
    colors=['#E50914', '#555555', '#831010'],
    autopct='%1.1f%%', textprops={'color': 'white'})
axes[1,1].set_title('Description Sentiment', color='white')
axes[1,1].set_facecolor('#1E1E1E')

# Plot 6 — Sentiment by Type
sentiment_type = df.groupby(['type', 'sentiment_label']).size().unstack()
sentiment_type.plot(kind='bar', ax=axes[1,2],
    color=['#E50914', '#555555', '#831010'])
axes[1,2].set_title('Sentiment by Content Type', color='white')
axes[1,2].set_facecolor('#1E1E1E')
axes[1,2].tick_params(colors='white')

plt.tight_layout()
plt.savefig('netflix_analysis.png', dpi=150,
    bbox_inches='tight', facecolor='#141414')
print("\n✅ Chart saved as netflix_analysis.png")

# ── Save enriched dataset ──────────────────────────────
df.to_csv('netflix_enriched.csv', index=False)
print("✅ Enriched dataset saved as netflix_enriched.csv")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
import warnings
warnings.filterwarnings('ignore')

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv('netflix_titles.csv')
df.fillna('Unknown', inplace=True)
print("✅ Data loaded")

# ── Genre Co-occurrence ────────────────────────────────
print("\n🎭 ANALYSIS — Genre Co-occurrence Matrix")

pairs = []
for genres in df['listed_in']:
    if genres != 'Unknown':
        genre_list = [g.strip() for g in genres.split(',')]
        for pair in combinations(genre_list, 2):
            pairs.append(sorted(pair))

pair_df = pd.DataFrame(pairs, columns=['Genre1', 'Genre2'])
co_matrix = pair_df.groupby(['Genre1', 'Genre2']).size().reset_index(name='count')
co_matrix = co_matrix.sort_values('count', ascending=False)

print("\nTop 15 Genre Pairs:")
print(co_matrix.head(15).to_string(index=False))

# ── Top Single Genres ──────────────────────────────────
print("\n🎬 Top 15 Individual Genres:")
all_genres = []
for genres in df['listed_in']:
    if genres != 'Unknown':
        for g in genres.split(','):
            all_genres.append(g.strip())

genre_series = pd.Series(all_genres)
top_genres = genre_series.value_counts().head(15)
print(top_genres)

# ── Visualizations ─────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(18, 8))
fig.patch.set_facecolor('#141414')
plt.suptitle('Netflix Genre Analysis', color='#E50914',
    fontsize=20, fontweight='bold')

# Plot 1 — Top 15 Genres
top_genres.plot(kind='barh', ax=axes[0], color='#E50914')
axes[0].set_title('Top 15 Individual Genres', color='white', fontsize=14)
axes[0].set_facecolor('#1E1E1E')
axes[0].tick_params(colors='white')
axes[0].set_xlabel('Count', color='white')
axes[0].invert_yaxis()

# Plot 2 — Top Genre Pairs
top_pairs = co_matrix.head(12)
top_pairs['pair'] = top_pairs['Genre1'] + ' +\n' + top_pairs['Genre2']
axes[1].barh(top_pairs['pair'], top_pairs['count'], color='#831010')
axes[1].set_title('Top 12 Genre Combinations', color='white', fontsize=14)
axes[1].set_facecolor('#1E1E1E')
axes[1].tick_params(colors='white')
axes[1].set_xlabel('Co-occurrence Count', color='white')
axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig('genre_analysis.png', dpi=150,
    bbox_inches='tight', facecolor='#141414')
print("\n✅ Genre chart saved as genre_analysis.png")

# ── Genre by Content Type ──────────────────────────────
print("\n📊 Genre breakdown by Movies vs TV Shows:")
for content_type in ['Movie', 'TV Show']:
    print(f"\n{content_type}:")
    type_genres = []
    for genres in df[df['type'] == content_type]['listed_in']:
        if genres != 'Unknown':
            for g in genres.split(','):
                type_genres.append(g.strip())
    print(pd.Series(type_genres).value_counts().head(5))
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv('netflix_titles.csv')
df.fillna('Unknown', inplace=True)
print("✅ Data loaded")

# ── Word Cloud from Descriptions ───────────────────────
all_text = ' '.join(df['description'].astype(str))
movie_text = ' '.join(df[df['type']=='Movie']['description'].astype(str))
tvshow_text = ' '.join(df[df['type']=='TV Show']['description'].astype(str))

# ── Generate Word Clouds ───────────────────────────────
wc_all = WordCloud(width=800, height=400, background_color='black',
    colormap='Reds', max_words=100).generate(all_text)

wc_movie = WordCloud(width=800, height=400, background_color='black',
    colormap='Reds', max_words=100).generate(movie_text)

wc_tv = WordCloud(width=800, height=400, background_color='black',
    colormap='Reds', max_words=100).generate(tvshow_text)

# ── Plot ───────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(20, 6))
fig.patch.set_facecolor('#141414')
plt.suptitle('Netflix Description Word Clouds',
    color='#E50914', fontsize=20, fontweight='bold')

axes[0].imshow(wc_all, interpolation='bilinear')
axes[0].set_title('All Content', color='white', fontsize=14)
axes[0].axis('off')

axes[1].imshow(wc_movie, interpolation='bilinear')
axes[1].set_title('Movies Only', color='white', fontsize=14)
axes[1].axis('off')

axes[2].imshow(wc_tv, interpolation='bilinear')
axes[2].set_title('TV Shows Only', color='white', fontsize=14)
axes[2].axis('off')

plt.tight_layout()
plt.savefig('wordcloud_analysis.png', dpi=150,
    bbox_inches='tight', facecolor='#141414')
print("✅ Word cloud saved as wordcloud_analysis.png")
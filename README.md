<p align="center">
  <img src="logo.png" alt="Netflix Logo" width="700"/>
</p>

<h1 align="center">Netflix Data Analysis — End-to-End Analytics Project</h1>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white"/>
  <img src="https://img.shields.io/badge/Microsoft-Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power-BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Dataset-8800%2B Titles-E50914?style=for-the-badge"/>
</p>

---

## 📌 Project Overview

A complete **end-to-end data analytics project** on the Netflix dataset covering **8,800+ titles** across **750+ countries**. This project goes beyond basic Excel analysis by combining SQL querying, Python-based sentiment analysis, genre co-occurrence modeling, and an interactive Power BI dashboard — all built to industry standards.

**Tools Used:** Microsoft Excel · SQL Server (SSMS) · Python 3.14 · Power BI Desktop

---

## 🗂️ Project Structure

```
Netflix-analysis/
│
├── 📄 README.md
├── 🖼️ logo.png
│
├── 📁 SQL/
│   └── NETFLIX_SQL.sql                     ← 15 business SQL queries
│
├── 📁 Excel/
│   └── netflix_cleaned.xlsx                ← Cleaned dataset
│
├── 📁 Python/
│   ├── 01_eda_sentiment_analysis.py        ← EDA + sentiment scoring
│   ├── 02_genre_cooccurrence_analysis.py   ← Genre pair analysis
│   ├── 03_description_wordcloud.py         ← Word cloud generation
│   └── requirements.txt                    ← Python dependencies
│
├── 📁 outputs/
│   ├── netflix_analysis.png                ← EDA charts
│   ├── genre_analysis.png                  ← Genre co-occurrence charts
│   ├── wordcloud_analysis.png              ← Word clouds
│   └── netflix_enriched.csv               ← Dataset with sentiment scores
│
├── 📁 CSV Exports/
│   ├── content_type.csv
│   ├── top_countries.csv
│   ├── ratings_breakdown.csv
│   ├── genre_breakdown.csv
│   ├── yearly_content.csv
│   └── india_yearly.csv
│
└── 📁 PowerBI/
    └── netflix_dashboard.pbix              ← Interactive dashboard
```

---

## 🔧 Phase 1 — Excel Data Cleaning

Raw CSV (`netflix_titles.csv`) was cleaned in Microsoft Excel:

- ✅ Removed duplicate records
- ✅ Handled nulls in `director`, `cast`, `country`, `rating` → replaced with `Unknown`
- ✅ Converted `date_added` text → proper Excel Date format using `DATEVALUE(TRIM())`
- ✅ Split `duration` → `Duration_Value` (numeric) + `Duration_Type` (min/Seasons)
- ✅ Added `content_type_flag` column for Power BI slicer filtering

---

## 🔍 Phase 2 — SQL Analysis (15 Business Queries)

All queries written in **SQL Server (SSMS)**.

| # | Business Question | Key Technique |
|---|---|---|
| 1 | Count Movies vs TV Shows | `GROUP BY`, `COUNT` |
| 2 | Most common rating per type | `RANK()`, `PARTITION BY` |
| 3 | Movies released in 2020 | `WHERE`, date filter |
| 4 | Top 5 countries by content | `TOP`, `ORDER BY` |
| 5 | Longest movie | `CAST`, `REPLACE`, `ORDER BY` |
| 6 | Content added in last 5 years | `DATEADD`, `GETDATE` |
| 7 | Content by director 'Rajiv Chilaka' | `LIKE` |
| 8 | TV Shows with 5+ seasons | String comparison |
| 9 | Content count per genre | `GROUP BY listed_in` |
| 10 | Yearly content releases in India | `LIKE '%India%'`, `TOP 5` |
| 11 | Movies that are documentaries | `LIKE '%Documentaries%'` |
| 12 | Content without a director | `IS NULL` |
| 13 | Salman Khan movies (last 10 years) | `LIKE`, `YEAR()` |
| 14 | Top 10 actors in Indian movies | `STRING_SPLIT`, `CROSS APPLY` |
| 15 | Bad vs Good content categorization | `CASE WHEN`, keyword search |

---

## 🐍 Phase 3 — Python Analysis

Three scripts adding analytical depth impossible in Excel alone:

### 01 — EDA + Sentiment Analysis
- Full exploratory data analysis across all 12 columns
- **TextBlob NLP sentiment scoring** on 8,800+ descriptions
- Finding: Netflix uses **more positive language for Movies** (49.6%) vs TV Shows (44.3%)
- Output: `netflix_analysis.png`, `netflix_enriched.csv`

### 02 — Genre Co-occurrence Analysis
- Splits multi-genre tags into individual genres
- Builds **genre pair co-occurrence matrix** using `itertools.combinations`
- Identifies which genre combinations appear most frequently together
- Output: `genre_analysis.png`

### 03 — Description Word Cloud
- Generates word clouds from all 8,800+ description texts
- Separate clouds for **Movies vs TV Shows** to compare language patterns
- Output: `wordcloud_analysis.png`

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run scripts
```bash
python 01_eda_sentiment_analysis.py
python 02_genre_cooccurrence_analysis.py
python 03_description_wordcloud.py
```

---

## 📈 Phase 4 — Power BI Dashboard

Industry-level interactive dashboard with **Netflix dark theme**.

**Theme:** `#000000` background · `#E50914` accent · `#FFFFFF` text

**Visuals included:**
| Visual | Type | Data Source |
|---|---|---|
| 6 KPI Cards | Card | DAX measures |
| Genres by Titles | Horizontal bar | genre_breakdown.csv |
| Ratings by Show ID | Horizontal bar | ratings_breakdown.csv |
| Netflix Logo | Image | logo.png |
| Movies & TV by Year | Area chart | netflix_cleaned.xlsx |
| Movie vs TV Show | Donut chart | netflix_cleaned.xlsx |
| Top 10 Countries | Treemap | top_countries.csv |

**DAX Measures:**
```dax
Total Titles = COUNTROWS(netflix_titles_cleaned)
Total Movies = CALCULATE(COUNTROWS(netflix_titles_cleaned), netflix_titles_cleaned[type] = "Movie")
Total TV Shows = CALCULATE(COUNTROWS(netflix_titles_cleaned), netflix_titles_cleaned[type] = "TV Show")
Total Ratings = DISTINCTCOUNT(netflix_titles_cleaned[rating])
Start Year = MIN(netflix_titles_cleaned[release_year])
End Year = MAX(netflix_titles_cleaned[release_year])
Total Genres = DISTINCTCOUNT(netflix_titles_cleaned[listed_in])
```

---

## 💡 Key Insights

- 🎬 **69.6%** of Netflix content is Movies vs **30.4%** TV Shows
- 🇺🇸 **USA leads** with 2,818 titles — nearly **3x India** (972)
- 📺 **TV-MA** is the most common rating with 3,207 titles
- 📈 Content additions **peaked in 2019** (2,016 titles) before declining
- 🎭 **Dramas & International Movies** is the largest genre category
- 🧠 **49.6% of Movie descriptions** use positive sentiment language
- 🇮🇳 India is the **2nd largest** content-producing country on Netflix

---

## 🛠️ How to Run

### SQL
```sql
-- Import netflix_titles.csv into SQL Server as table 'Netflix'
-- Open NETFLIX_SQL.sql in SSMS and run
```

### Python
```bash
cd Python
pip install -r requirements.txt
python 01_eda_sentiment_analysis.py
python 02_genre_cooccurrence_analysis.py
python 03_description_wordcloud.py
```

### Power BI
```
1. Open netflix_dashboard.pbix in Power BI Desktop
2. Update data source path if needed
3. Click Refresh
```

---

## 💻 Requirements

| Tool | Version |
|---|---|
| SQL Server | 2019+ |
| SSMS | 18+ |
| Microsoft Excel | 2016+ |
| Python | 3.8+ |
| Power BI Desktop | Latest (free) |

Dataset: [Kaggle — Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## 👤 Author

**Anshuman Singh**  
Pre-final year B.Tech Computer Engineering · Galgotias University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/anshuman-singh-9393102a5)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/Anshuman0509)

---

<p align="center">Made with ❤️ for data exploration and portfolio building</p>

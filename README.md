<p align="center">
  <img src="logo.png" alt="Netflix Logo" width="700"/>
</p>

<h1 align="center">Netflix Data Analysis — End-to-End Analytics Project</h1>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white"/>
  <img src="https://img.shields.io/badge/Microsoft-Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power-BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/Dataset-8800%2B Titles-E50914?style=for-the-badge"/>
</p>

---

## 📌 Project Overview

A complete end-to-end data analytics project on the Netflix dataset covering **8,800+ titles** across **750+ countries**. The project follows the full analyst workflow — raw data ingestion, cleaning in Excel, deep-dive SQL analysis, and an interactive Power BI dashboard built to industry standards.

**Tools Used:** Microsoft Excel · SQL Server (SSMS) · Power BI Desktop

---

## 🗂️ Project Structure

```
Netflix-analysis/
│
├── 📄 README.md
├── 🖼️ logo.png
│
├── 📁 SQL/
│   ├── NETFLIX_SQL.sql          ← 15 business queries
│   └── Business Problems.sql    ← Problem statements
│
├── 📁 Excel/
│   └── netflix_cleaned.xlsx     ← Cleaned dataset
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
    └── netflix_dashboard.pbix   ← Interactive dashboard
```

---

## 📊 Dashboard Preview

> **Industry-level Power BI dashboard with Netflix dark theme**

| KPI | Value |
|---|---|
| Total Titles | 8,809 |
| Total Ratings | 18 unique |
| Start Year | 1925 |
| End Year | 2021 |
| Total Genres | 515 |
| Countries | 749 |

**Dashboard pages include:**
- KPI cards row with all key metrics
- Genres by Titles (horizontal bar chart)
- Ratings by Show ID (bar chart)
- Movies & TV Shows by Release Year (area chart)
- Movie vs TV Show split (donut chart)
- Top 10 Countries by content (treemap)

---

## 🔧 Phase 1 — Excel Data Cleaning

Raw CSV (`netflix_titles.csv`) was cleaned using Microsoft Excel:

- ✅ Removed duplicate records using Remove Duplicates
- ✅ Handled null values in `director`, `cast`, `country`, `rating` columns → replaced with `Unknown`
- ✅ Converted `date_added` text to proper Excel Date format using `DATEVALUE(TRIM())`
- ✅ Split `duration` column into `Duration_Value` (numeric) and `Duration_Type` (min/Seasons)
- ✅ Added `content_type_flag` column for slicer-friendly filtering in Power BI
- ✅ Saved cleaned output as `netflix_cleaned.xlsx`

---

## 🔍 Phase 2 — SQL Analysis (15 Business Queries)

All queries written in **Microsoft SQL Server (SSMS)** against a database named `Netflix`.

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

## 📈 Phase 3 — Power BI Dashboard

Interactive dashboard built in Power BI Desktop with a **Netflix dark theme** (`#000000` background, `#E50914` accent).

**Data sources connected:**
- `netflix_cleaned.xlsx` — main dataset (8,809 rows)
- 6 CSV exports from SQL queries

**DAX Measures created:**
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

- 🎬 **69.6%** of Netflix content is Movies, **30.4%** is TV Shows
- 🇺🇸 **United States** leads with 2,818 titles — nearly 3x India (972)
- 📺 **TV-MA** is the most common rating with 3,207 titles
- 📈 Content additions **peaked in 2019** before declining post-2020
- 🎭 **Dramas & International Movies** is the largest genre category
- 🇮🇳 India is the **2nd largest** content-producing country on Netflix

---

## 🛠️ How to Use

### SQL
1. Import `netflix_titles.csv` into SQL Server as table `Netflix`
2. Open `NETFLIX_SQL.sql` in SSMS
3. Run queries individually or all at once

### Power BI
1. Open `netflix_dashboard.pbix` in Power BI Desktop
2. Update data source path if needed (`Transform Data → Data Source Settings`)
3. Click `Refresh` to reload data

---

## 💻 Requirements

| Tool | Version |
|---|---|
| Microsoft SQL Server | 2019 or later |
| SQL Server Management Studio | 18+ |
| Microsoft Excel | 2016 or later |
| Power BI Desktop | Latest (free) |

Dataset available on [Kaggle — Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## 👤 Author

**Anshuman Singh**
Pre-final year B.Tech Computer Engineering · Galgotias University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/anshuman-singh-9393102a5)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/Anshuman0509)

---

<p align="center">Made with ❤️ for data exploration and portfolio building</p>

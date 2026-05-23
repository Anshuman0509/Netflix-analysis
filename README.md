![Netflix Banner](assets/logo.png)

# 🎬 Netflix SQL Analysis

A collection of SQL queries to explore and analyze the Netflix dataset using Microsoft SQL Server.

---

## 📁 File

| File | Description |
|------|-------------|
| `NETFLIX_SQL.sql` | All SQL queries for Netflix data analysis |

---

## 📊 Dataset

The dataset contains Netflix titles with the following columns:

- `show_id` — Unique ID for each title
- `type` — Movie or TV Show
- `title` — Name of the content
- `director` — Director(s)
- `cast` — Actors/actresses
- `country` — Country of production
- `date_added` — Date added to Netflix
- `release_year` — Year of release
- `rating` — Content rating (e.g. PG, TV-MA)
- `duration` — Runtime (minutes for movies, seasons for TV shows)
- `listed_in` — Genre(s)
- `description` — Short summary

---

## 🔍 Queries Covered

| # | Question |
|---|----------|
| 1 | Count the number of Movies vs TV Shows |
| 2 | Find the most common rating for movies and TV shows |
| 3 | List all movies released in a specific year (e.g. 2020) |
| 4 | Find the top 5 countries with the most content on Netflix |
| 5 | Identify the longest movie |
| 6 | Find content added in the last 5 years |
| 7 | Find all movies/TV shows by director 'Rajiv Chilaka' |
| 8 | List all TV shows with more than 5 seasons |
| 9 | Count the number of content items in each genre |
| 10 | Find each year and the average number of content releases in India |
| 11 | List all movies that are documentaries |
| 12 | Find all content without a director |
| 13 | Find how many movies actor 'Salman Khan' appeared in the last 10 years |
| 14 | Find the top 10 actors in the highest number of Indian movies |
| 15 | Categorize content based on keywords 'kill' and 'violence' in description |

---

## 🛠️ How to Use

1. Import the Netflix dataset into a database named `Netflix`
2. Open `NETFLIX_SQL.sql` in SQL Server Management Studio (SSMS)
3. Run queries individually or all at once

---

## 💻 Requirements

- Microsoft SQL Server
- SQL Server Management Studio (SSMS)
- Netflix dataset (available on [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows))

---

## 👤 Author

Made with ❤️ for data exploration and SQL practice.

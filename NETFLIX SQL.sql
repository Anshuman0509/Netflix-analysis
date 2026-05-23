SELECT * FROM Netflix
ORDER BY CAST(SUBSTRING(show_id, 2, LEN(show_id)) AS INT) ASC;



--1. Count the number of Movies vs TV Shows

SELECT type, COUNT(*) AS total_count
FROM Netflix
GROUP BY type;



--2. Find the most common rating for movies and TV shows
USE Netflix
SELECT TYPE, RATING, COUNT(*) AS count
FROM Netflix
GROUP BY type, rating
ORDER BY type, count DESC;

SELECT type, rating
FROM(
    SELECT type, rating, COUNT(*) AS cnt,
         RANK() OVER (PARTITION BY type ORDER BY COUNT(*) DESC) AS rnk
         FROM Netflix
         GROUP BY type, rating
         ) ranked
         WHERE rnk =1

--3. List all movies released in a specific year (e.g., 2020)

SELECT title, release_year, 
FROM Netflix
WHERE type = 'Movie'
AND release_year= 2020
;

--4. Find the top 5 countries with the most content on Netflix

SELECT TOP 5 country , Count(*) as total_content
FROM Netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_content DESC;

--5. Identify the longest movie

SELECT TOP 1 title, duration
FROM Netflix
where TYPE= 'Movie'
AND duration is not NULL
ORDER BY CAST(REPLACE(duration, ' min', '') AS INT) DESC;

--6. Find content added in the last 5 years

SELECT title, date_added
FROM Netflix
WHERE CAST(date_added AS DATE) >= DATEADD(YEAR, -5, GETDATE());

--7. Find all the movies/TV shows by director 'Rajiv Chilaka'!

SELECT title, type, director
FROM Netflix 
WHERE director LIKE '%Rajiv Chilaka%'


--8. List all TV shows with more than 5 seasons

SELECT title, duration , type
FROM Netflix
WHERE type= 'TV Show'
AND duration > '5Seasons';


--9. Count the number of content items in each genre

SELECT listed_in AS genre, COUNT(*) AS total
FROM Netflix
group by listed_in
ORDER BY total DESC;


--10.Find each year and the average numbers of content release in India on netflix.

SELECT TOP 5 release_year,
COUNT(*) AS total_released
FROM Netflix
WHERE country  LIKE '%India%'
GROUP BY release_year ORDER BY total_released DESC;

--11. List all movies that are documentaries

SELECT title, listed_in
FROM Netflix
WHERE type = 'Movie'
  AND listed_in LIKE '%Documentaries%';


--12. Find all content without a director

SELECT title, type, director
FROM Netflix
WHERE director IS NULL;

--13. Find how many movies actor 'Salman Khan' appeared in last 10 years!

SELECT title, release_year, cast
FROM Netflix
WHERE type = 'Movie'
  AND cast LIKE '%Salman Khan%'
  AND release_year >= YEAR(GETDATE()) - 10;

--14. Find the top 10 actors who have appeared in the highest number of movies produced in India.

SELECT TOP 10 
TRIM(value) AS actor,
COUNT(*) AS appearences
FROM Netflix 
CROSS APPLY STRING_SPLIT (cast, ',')
WHERE Country LIKE '%India%'
AND type = 'Movie'
AND cast is NOT NULL
GROUP BY TRIM(value)
ORDER BY appearences DESC;


--15.Categorize the content based on the presence of the keywords 'kill' and 'violence' in the description field. Label content containing these keywords as 'Bad' and all other content as 'Good'. Count how many items fall into each category.

SELECT category ,
COUNT(*) AS content_count
FROM(
SELECT CASE WHEN description LIKE '%kill%'
OR description LIKE '%violence%'
THEN 'Bad'
ELSE 'Good'
END AS category
FROM Netflix
) AS categorized 
GROUP BY  category;


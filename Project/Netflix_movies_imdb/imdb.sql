-- Netflie Movie Data
-- Question 1: How many movies and shows are in the dataset?
SELECT
    type, 
    COUNT(type) as Total_type
FROM imdb_movies_shows_main
GROUP BY type;

-- Question 1.2: How many movies have ratings in the dataset?
SELECT
	ROUND(imdb_score) as Rating,
    COUNT(imdb_score) As Total_rate
FROM imdb_movies_shows_main
GROUP BY Rating
ORDER BY Total_rate DESC;

-- Question 1.3 How many drama and romance genres?
SELECT
	genres,
    COUNT(*) AS Total_genres
FROM imdb_movies_shows_main
WHERE genres IN ('drama', 'romance')
GROUP BY genres
ORDER BY Total_genres DESC;



-- Question 2: Which movies have the highest top 10 scores?
SELECT
    title,
    release_year,
    imdb_score
FROM imdb_movies_shows_main
ORDER BY imdb_score DESC
LIMIT 10;


-- Question 3: Which movies have the top 10 scores in US and JP?
SELECT
	DISTINCT production_countries as countries,
    title,
    imdb_score
FROM imdb_movies_shows_main
WHERE production_countries IN ('US', 'JP')
Order BY imdb_score DESC
LIMIT 10;

-- Question 4: How many movies were released in 2000?
SELECT
	title,
    type,
    release_year,
    imdb_score
FROM imdb_movies_shows_main
WHERE release_year IN (2000)
ORDER BY imdb_score DESC;

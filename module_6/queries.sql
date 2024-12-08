SELECT DISTINCT c1.name, m1.title, m2.title
  FROM movies m1, movies m2, credits c1, credits c2
 WHERE c1.name = c2.name
   AND m1.id < m2.id
   AND m1.id = c1.movie_id
   AND m2.id = c2.movie_id
 ORDER BY c2.name;

WITH movies_and_credits AS (
  SELECT *
    FROM movies INNER JOIN credits 
      ON movies.id = credits.movie_id
)
SELECT m1.name, m1.title, m2.title
  FROM movies_and_credits m1, movies_and_credits m2
 WHERE m1.name = m2.name AND m1.id < m2.id
 ORDER BY m1.name;
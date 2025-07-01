— 1. Full Table
SELECT * FROM "AwsDataCatalog"."spotify"."datawarehouse" ;

—2. Top 10 Most Popular Artists (Average Artist Popularity)
SELECT artist_id, AVG(CAST(artist_popularity AS INT)) AS avg_popularity
FROM datawarehouse
GROUP BY artist_id
ORDER BY avg_popularity DESC
LIMIT 10;

—3. Albums with the Most Tracks
SELECT album_name, COUNT(track_id) AS track_count
FROM datawarehouse
GROUP BY album_name
ORDER BY track_count DESC
LIMIT 10;

—4. Most Common Genres
SELECT genre, COUNT(*) AS genre_count
FROM datawarehouse
GROUP BY genre
ORDER BY genre_count DESC
LIMIT 10;

—5. Average Track Popularity per Album
SELECT album_name, AVG(CAST(track_popularity AS INT)) AS avg_popularity
FROM datawarehouse
GROUP BY album_name
ORDER BY avg_popularity DESC
LIMIT 10;
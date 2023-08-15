-- Display same scores using COUNT, ORDER BY, GROUP BY
-- DML query to display the number of records with same score
SELECT score,COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY score DESC;

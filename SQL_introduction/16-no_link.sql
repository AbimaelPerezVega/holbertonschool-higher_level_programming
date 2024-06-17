-- List all records from second_table where name is not NULL or empty
USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

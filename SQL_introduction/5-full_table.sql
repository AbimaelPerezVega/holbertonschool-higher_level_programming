-- Print full table description for first_table
SELECT CONCAT('Table   Create Table') AS 'Table';
SELECT CONCAT(TABLE_NAME, '     ', CREATE_STATEMENT) AS 'Create Table'
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'your_database_name'
AND TABLE_NAME = 'first_table';
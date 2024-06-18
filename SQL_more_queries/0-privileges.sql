-- Ensure user_0d_1 exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Ensure user_0d_2 exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Grant some privileges to user_0d_2 (for example, SELECT)
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

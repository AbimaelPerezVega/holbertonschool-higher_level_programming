-- Check if user 'user_0d_1'@'localhost' already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1'@'localhost'
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

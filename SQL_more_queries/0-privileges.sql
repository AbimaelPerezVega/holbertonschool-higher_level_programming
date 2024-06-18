-- Grant some privileges to user_0d_1
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';

-- Grant some privileges to user_0d_2
GRANT SELECT ON * . * TO 'user_0d_2'@'localhost';

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

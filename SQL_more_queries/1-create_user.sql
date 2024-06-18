-- Check if user 'user_0d_1'@'localhost' already exists
SELECT EXISTS (
    SELECT 1
    FROM mysql.user
    WHERE user = 'user_0d_1' AND host = 'localhost'
) INTO @user_exists;

-- If the user does not exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

-- Grant all privileges to 'user_0d_1'@'localhost'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;

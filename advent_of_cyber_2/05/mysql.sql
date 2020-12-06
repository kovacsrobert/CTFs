DROP DATABASE IF EXISTS test;
CREATE DATABASE test DEFAULT CHARACTER SET 'utf8mb4' DEFAULT COLLATE 'utf8mb4_general_ci';
USE test;
CREATE TABLE users (name VARCHAR(50) PRIMARY KEY, password VARCHAR(50) NOT NUll);
INSERT INTO users (name, password) VALUES ('admin', 'verysecret');
INSERT INTO users (name, password) VALUES ('user1', 'password1');
INSERT INTO users (name, password) VALUES ('user2', 'password2');
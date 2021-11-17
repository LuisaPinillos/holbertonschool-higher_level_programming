-- Script that creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
    id INT DEFAULT 0,
    name VARCHAR(256) DEFAULT NULL,
    score INT DEFAULT 0
);

INSERT INTO second_table 
    (`id`,`name`,`score`)
VALUES 
    ("1", "jhon", "10"),
    ("2", "Alex", "3"),
    ("3", "Bob", "14"),
    ("4", "George", "8")

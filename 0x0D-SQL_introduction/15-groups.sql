-- Script that lists the number of records with the 
-- same score in the table second_table
SELECT score,count(score) AS 'number' FROM second_table GROUP BY score HAVING count(score)>1;

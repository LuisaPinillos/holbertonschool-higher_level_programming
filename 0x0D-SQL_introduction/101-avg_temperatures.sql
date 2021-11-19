-- Import in hbtn_0c_0 database temperatures table dump
-- Script that displays the average temperature per city (descending).
SELECT city, AVG(value) AS avg_temp
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

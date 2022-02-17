/*
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. 
Your result cannot contain duplicates.
*/

-- Query
SELECT distinct city FROM station WHERE City like '%[aeiou]';

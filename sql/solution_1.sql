/*
Query all columns for all American cities in the CITY table with populations larger than 100000. 
The CountryCode for America is USA.
*/

-- Query
select * from city where countrycode='usa' and population >100000;
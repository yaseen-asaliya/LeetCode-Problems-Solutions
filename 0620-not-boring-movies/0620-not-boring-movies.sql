# Write your MySQL query statement below

select * from Cinema where id % 2 = 1 and not description like '%boring%' order by rating desc;

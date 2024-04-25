# Write your MySQL query statement below
select b.id
from weather a, weather b 
where date_sub(b.recordDate,Interval 1 Day)=a.recordDate
and b.temperature > a.temperature

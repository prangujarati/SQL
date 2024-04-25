# Write your MySQL query statement below
select round(count(distinct(player_id))/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) as fraction from activity where 
(player_id, event_date) in 
(select player_id, date_add(min(event_date),interval 1 day) as a
from activity
group by player_id)

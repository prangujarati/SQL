# Write your MySQL query statement below
select person_name from (
SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) a
where a.cumulative_weight <= 1000
order by a.cumulative_weight desc
limit 1
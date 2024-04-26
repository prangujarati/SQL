# Write your MySQL query statement below
#select a.product_id, min(a.year) as first_year, a.quantity, a.price
#from sales a
#join product b
#on a.product_id=b.product_id
#group by product_id
select a.product_id, a.year as first_year, a.quantity, a.price
from sales a
join 
(select product_id, min(year) as min_year
from sales 
group by product_id) b
on a.product_id=b.product_id and a.year=b.min_year





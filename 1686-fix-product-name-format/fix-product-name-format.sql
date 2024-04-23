# Write your MySQL query statement below
select trim(lower(product_name)) as product_name,
left(sale_date,7) as sale_date,
count(sale_id) as total
from sales
group by trim(lower(product_name)), left(sale_date,7)
order by product_name, sale_date
# Write your MySQL query statement below
select distinct left(order_date,7) as month, count(order_id) as order_count, count(distinct(customer_id)) as customer_count
from orders  where invoice>20
group by month
order by month 
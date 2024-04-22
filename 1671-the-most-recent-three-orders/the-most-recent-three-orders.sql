# Write your MySQL query statement below
-- select c.name, c.customer_id, o.order_id, o.order_date
-- from customers c inner join orders o 
-- on c.customer_id=o.customer_id
-- group by c.name
-- order by o.order_date desc

select name as customer_name, customer_id, order_id, order_date
from (
    select name,c.customer_id,o.order_id,o.order_date,
    rank() over (partition by c.customer_id order by order_date desc) as rnk
    from customers c right join orders o
    on c.customer_id=o.customer_id
)t
where rnk in(1,2,3)
order by name,customer_id,order_date desc
# Write your MySQL query statement below
select seller_name as SELLER_NAME from seller where seller_id not in (
     select seller_id from orders where YEAR(sale_date)=2020
)
order by seller_name
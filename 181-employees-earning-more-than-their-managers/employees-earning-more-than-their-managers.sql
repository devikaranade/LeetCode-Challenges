# Write your MySQL query statement below
select a.name as 'Employee' from 
employee as A, employee as B where 
a.managerId=b.id and 
a.salary>b.salary
# Write your MySQL query statement below
select d.name as Department, e.name as Employee, Salary from employee e inner join department d
on e.departmentId=d.id
where e.departmentId=d.id
and (e.departmentId, salary) IN (
    select departmentId, max(salary)
    from employee 
    group by departmentId
) 


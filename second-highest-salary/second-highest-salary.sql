# Write your MySQL query statement below
select (select distinct Salary from Employee e1 ORDER BY Salary DESC
LIMIT 1 OFFSET 1) as SecondHighestSalary;
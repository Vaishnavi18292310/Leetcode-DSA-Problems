# Write your MySQL query statement below
select e1.name
from employee e1 
join employee m
on e1.id = m.managerID
group by m.managerId
having count(*)>=5;
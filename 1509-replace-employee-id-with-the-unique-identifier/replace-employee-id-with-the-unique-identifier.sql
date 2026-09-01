# Write your MySQL query statement below
select Eu. unique_id, E.name
from Employees E
Left join EmployeeUNI Eu
on E.id=Eu.id;
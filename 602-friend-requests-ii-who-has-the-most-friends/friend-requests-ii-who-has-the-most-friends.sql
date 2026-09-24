# Write your MySQL query statement below
with all_users as(
    select requester_id as user_id
    from RequestAccepted 

    union all
    select accepter_id as user_id
    from RequestAccepted 
)

select user_id as id,
count(*) as num
from all_users
group by user_id
order by num desc
limit 1;
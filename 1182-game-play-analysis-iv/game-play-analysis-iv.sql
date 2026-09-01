# Write your MySQL query statement below
select
round(
    count(distinct a.player_id)/
    (select count(distinct player_id)
    from activity)
    ,2) as fraction
from activity a

join(
    select player_id,
    min(event_date) as first_date
    from activity
    group by player_id
)first_log_in
on a.player_id=first_log_in.player_id
and a.event_date=first_log_in.first_date+interval 1 day;
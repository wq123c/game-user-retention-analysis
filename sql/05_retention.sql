SELECT
t0.register_date,
t0.new_users,
IFNULL(t1.day1_users,0) AS day1_users,

ROUND(
IFNULL(t1.day1_users,0)/t0.new_users*100,
2
) AS day1_rate,

IFNULL(t3.day3_users,0) AS day3_users,

ROUND(
IFNULL(t3.day3_users,0)/t0.new_users*100,
2
) AS day3_rate,

IFNULL(t7.day7_users,0) AS day7_users,

ROUND(
IFNULL(t7.day7_users,0)/t0.new_users*100,
2
) AS day7_rate

FROM

(
SELECT
register_date,
COUNT(DISTINCT user_id) AS new_users
FROM game_user_log
GROUP BY register_date
)t0

LEFT JOIN
(
SELECT
a.register_date,
COUNT(DISTINCT a.user_id) AS day1_users
FROM game_user_log a
JOIN game_user_log b
ON a.user_id=b.user_id
AND b.login_date=DATE_ADD(a.register_date,INTERVAL 1 DAY)
GROUP BY a.register_date
)t1

ON t0.register_date=t1.register_date

LEFT JOIN
(
SELECT
a.register_date,
COUNT(DISTINCT a.user_id) AS day3_users
FROM game_user_log a
JOIN game_user_log b
ON a.user_id=b.user_id
AND b.login_date=DATE_ADD(a.register_date,INTERVAL 3 DAY)
GROUP BY a.register_date
)t3

ON t0.register_date=t3.register_date

LEFT JOIN
(
SELECT
a.register_date,
COUNT(DISTINCT a.user_id) AS day7_users
FROM game_user_log a
JOIN game_user_log b
ON a.user_id=b.user_id
AND b.login_date=DATE_ADD(a.register_date,INTERVAL 7 DAY)
GROUP BY a.register_date
)t7

ON t0.register_date=t7.register_date

ORDER BY t0.register_date;
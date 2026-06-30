SELECT
    register_date,
    COUNT(DISTINCT user_id) AS new_users
FROM game_user_log
GROUP BY register_date
ORDER BY register_date;
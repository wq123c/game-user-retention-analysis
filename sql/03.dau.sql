SELECT
    login_date,
    COUNT(DISTINCT user_id) AS dau
FROM game_user_log
GROUP BY login_date
ORDER BY login_date;
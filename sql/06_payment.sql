SELECT
    dau.login_date,

    dau.dau,

    IFNULL(pay.paying_users,0) AS paying_users,

    ROUND(
        IFNULL(pay.paying_users,0) / dau.dau * 100,
        2
    ) AS payment_rate,

    IFNULL(revenue.total_revenue,0) AS total_revenue,

    ROUND(
        IFNULL(revenue.total_revenue,0) / dau.dau,
        2
    ) AS arpu,

    ROUND(
        IFNULL(revenue.total_revenue,0)
        /
        NULLIF(pay.paying_users,0),
        2
    ) AS arppu

FROM

(
    SELECT
        login_date,
        COUNT(DISTINCT user_id) AS dau
    FROM game_user_log
    GROUP BY login_date
) dau

LEFT JOIN

(
    SELECT
        login_date,
        COUNT(DISTINCT user_id) AS paying_users
    FROM game_user_log
    WHERE pay_amount > 0
    GROUP BY login_date
) pay

ON dau.login_date = pay.login_date

LEFT JOIN

(
    SELECT
        login_date,
        SUM(pay_amount) AS total_revenue
    FROM game_user_log
    GROUP BY login_date
) revenue

ON dau.login_date = revenue.login_date

ORDER BY dau.login_date;
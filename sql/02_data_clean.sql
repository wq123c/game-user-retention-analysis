-- 是否有空值
SELECT *
FROM game_user_log
WHERE user_id IS NULL
   OR register_date IS NULL
   OR login_date IS NULL;
   
-- 是否有重复数据
SELECT
user_id,
login_date,
COUNT(*)
FROM game_user_log
GROUP BY user_id, login_date
HAVING COUNT(*) > 1;

-- 是否存在异常充值
SELECT *
FROM game_user_log
WHERE pay_amount < 0;

-- 是否存在异常等级
SELECT *
FROM game_user_log
WHERE level < 1
   OR level > 100;
   

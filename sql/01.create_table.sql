CREATE DATABASE game_analysis;
USE game_analysis;

-- 创建表
CREATE TABLE game_user_log (
    user_id INT,
    register_date DATE,
    login_date DATE,
    level INT,
    pay_amount DECIMAL(10,2),
    channel VARCHAR(30),
    device VARCHAR(20),
    country VARCHAR(30)
);
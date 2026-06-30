import random
from datetime import datetime, timedelta

import pandas as pd

# 固定随机种子
random.seed(2026)

# 用户数量
NUM_USERS = 5000

# 注册开始日期
START_DATE = datetime(2025, 1, 1)

# 注册渠道
channels = [
    "App Store",
    "Huawei",
    "Xiaomi",
    "OPPO",
    "Vivo",
    "Official Website"
]

# 设备
devices = [
    "iOS",
    "Android"
]

# 国家（地区）
countries = [
    "China",
    "Japan",
    "Singapore",
    "Malaysia"
]

# 存放所有行为日志
data = []

for user_id in range(100001, 100001 + NUM_USERS):

    while True:

        offset = random.randint(0, 30)

        register_date = START_DATE + timedelta(days=offset)

        # 周末注册概率更高
        if register_date.weekday() >= 5:

            if random.random() < 0.7:
                break

        else:

            if random.random() < 0.3:
                break

    channel = random.choice(channels)
    device = random.choice(devices)
    country = random.choice(countries)

    r = random.random()

    if r < 0.40:
        active_days = random.randint(1, 2)

    elif r < 0.70:
        active_days = random.randint(3, 5)

    elif r < 0.90:
        active_days = random.randint(6, 10)

    else:
        active_days = random.randint(11, 15)
    level = 1
    is_payer = random.random() < 0.20
    for day in range(active_days):

        login_date = register_date + timedelta(days=day)

        if day > 0:
            level += random.randint(0, 1)

        level = min(level, 100)

        if is_payer and random.random() < 0.15:
            pay_amount = random.choice([6, 12, 30, 68, 128, 198, 328])
        else:
            pay_amount = 0

        data.append({
            "user_id": user_id,
            "register_date": register_date.date(),
            "login_date": login_date.date(),
            "level": level,
            "pay_amount": pay_amount,
            "channel": channel,
            "device": device,
            "country": country
        })

# 转换为 DataFrame
df = pd.DataFrame(data)

# 导出 CSV 文件
df.to_csv(
    "../data/game_user_log.csv",
    index=False,
    encoding="utf-8-sig"
)
print(f"共生成 {len(df)} 条行为日志。")

print(df.head())

print(df.groupby("user_id").head(5))
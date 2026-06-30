import pandas as pd

# ==========================
# 读取SQL分析结果
# ==========================

payment_df = pd.read_excel("../data/payment_analysis.xlsx")

print(payment_df.head())

print(payment_df.info())

print(payment_df.describe())

print("\n========== 平均指标 ==========")

print(
    payment_df[
        [
            "payment_rate",
            "arpu",
            "arppu"
        ]
    ].mean()
)
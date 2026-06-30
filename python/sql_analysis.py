import pandas as pd

# ==========================
# 读取SQL分析结果
# ==========================

retention_df = pd.read_excel("../data/retention_analysis.xlsx")

# ==========================
# 查看数据
# ==========================

print("========== 前5行 ==========")
print(retention_df.head())

print("\n========== 数据结构 ==========")
print(retention_df.info())

print("\n========== 缺失值 ==========")
print(retention_df.isnull().sum())

print("\n========== 描述统计 ==========")
print(retention_df.describe())

print("\n========== 平均留存率 ==========")
print(
    retention_df[
        [
            "day1_rate",
            "day3_rate",
            "day7_rate"
        ]
    ].mean()
)
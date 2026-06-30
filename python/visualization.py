import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
retention_df = pd.read_excel("../data/retention_analysis.xlsx")

# 创建画布
plt.figure(figsize=(12,6))

# Day1
plt.plot(
    retention_df["register_date"],
    retention_df["day1_rate"],
    marker="o",
    linewidth=2,
    label="Day1 Retention"
)

# Day3
plt.plot(
    retention_df["register_date"],
    retention_df["day3_rate"],
    marker="s",
    linewidth=2,
    label="Day3 Retention"
)

# Day7
plt.plot(
    retention_df["register_date"],
    retention_df["day7_rate"],
    marker="^",
    linewidth=2,
    label="Day7 Retention"
)

# 图表设置
plt.title("User Retention Rate Trend")
plt.xlabel("Register Date")
plt.ylabel("Retention Rate (%)")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()

# 保存图片
plt.savefig(
    "../images/retention_rate_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
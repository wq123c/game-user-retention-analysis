import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 读取数据
# ==========================

df = pd.read_excel("../data/new_users.xlsx")

df["register_date"] = pd.to_datetime(df["register_date"])

# ==========================
# 新增用户趋势图
# ==========================

plt.figure(figsize=(12,6))

plt.plot(
    df["register_date"],
    df["new_users"],
    marker="s",
    linewidth=2
)

plt.title("Daily New Users Trend")
plt.xlabel("Register Date")
plt.ylabel("New Users")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "../images/new_users_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
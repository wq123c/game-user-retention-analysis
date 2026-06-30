import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 读取数据
# ==========================

df = pd.read_excel("../data/dau.xlsx")

df["login_date"] = pd.to_datetime(df["login_date"])

# ==========================
# DAU趋势图
# ==========================

plt.figure(figsize=(12,6))

plt.plot(
    df["login_date"],
    df["dau"],
    marker="o",
    linewidth=2
)

plt.title("Daily Active Users Trend")
plt.xlabel("Login Date")
plt.ylabel("DAU")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "../images/dau_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 读取数据
# ==========================

df = pd.read_excel("../data/payment_analysis.xlsx")

# 日期转换（保险起见）
df["login_date"] = pd.to_datetime(df["login_date"])


# ==========================
# 图1：每日收入趋势
# ==========================

plt.figure(figsize=(12,6))

plt.plot(
    df["login_date"],
    df["total_revenue"],
    marker="o",
    linewidth=2
)

plt.title("Daily Revenue Trend")
plt.xlabel("Login Date")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "../images/daily_revenue_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================
# 图2：每日付费率
# ==========================

plt.figure(figsize=(12,6))

plt.plot(
    df["login_date"],
    df["payment_rate"],
    marker="s",
    linewidth=2
)

plt.title("Payment Rate Trend")
plt.xlabel("Login Date")
plt.ylabel("Payment Rate (%)")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "../images/payment_rate_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================
# 图3：ARPU趋势
# ==========================

plt.figure(figsize=(12,6))

plt.plot(
    df["login_date"],
    df["arpu"],
    marker="^",
    linewidth=2
)

plt.title("ARPU Trend")
plt.xlabel("Login Date")
plt.ylabel("ARPU")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "../images/arpu_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================
# 图4：ARPPU趋势
# ==========================

plt.figure(figsize=(12,6))

plt.plot(
    df["login_date"],
    df["arppu"],
    marker="D",
    linewidth=2
)

plt.title("ARPPU Trend")
plt.xlabel("Login Date")
plt.ylabel("ARPPU")

plt.xticks(rotation=45)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "../images/arppu_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
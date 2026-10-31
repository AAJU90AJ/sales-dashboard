import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("sales.csv", parse_dates=["date"])
df["revenue"] = df["quantity"] * df["price"]

total = df["revenue"].sum()
print(f"Total revenue: ₹{total:,.0f}")

top = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print("\nTop products:\n", top)
print("\nShare %:\n", (top/total*100).round(1))

df["month"] = df["date"].dt.to_period("M")
monthly = df.groupby("month")["revenue"].sum()
print("\nMonthly revenue:\n", monthly)

top.plot(kind="bar", color="steelblue")
plt.title("Revenue by Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.close()

monthly.index = monthly.index.astype(str)
monthly.plot(kind="line", marker="o", color="green")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_trend.png")
plt.close()

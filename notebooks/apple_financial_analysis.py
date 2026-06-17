# Apple Financial Analysis & 3-Year Forecast
# Author: Uday Bhaskar Kokkera

import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

df = pd.read_csv("data/processed/apple_financials_clean.csv")

# --------------------------------------------------
# 2. Calculate financial ratios and KPIs
# --------------------------------------------------

df["revenue_growth_pct"] = df["revenue"].pct_change() * 100
df["gross_margin_pct"] = df["gross_profit"] / df["revenue"] * 100
df["operating_margin_pct"] = df["operating_income"] / df["revenue"] * 100
df["net_margin_pct"] = df["net_income"] / df["revenue"] * 100
df["current_ratio"] = df["current_assets"] / df["current_liabilities"]
df["debt_to_equity"] = df["total_liabilities"] / df["shareholders_equity"]
df["free_cash_flow_margin_pct"] = df["free_cash_flow"] / df["revenue"] * 100
df["capex_as_pct_of_revenue"] = df["capital_expenditures"] / df["revenue"] * 100
df["return_on_assets_pct"] = df["net_income"] / df["total_assets"] * 100
df["return_on_equity_pct"] = df["net_income"] / df["shareholders_equity"] * 100

# Round calculated metrics
ratio_columns = [
    "revenue_growth_pct",
    "gross_margin_pct",
    "operating_margin_pct",
    "net_margin_pct",
    "current_ratio",
    "debt_to_equity",
    "free_cash_flow_margin_pct",
    "capex_as_pct_of_revenue",
    "return_on_assets_pct",
    "return_on_equity_pct"
]

df[ratio_columns] = df[ratio_columns].round(2)

# --------------------------------------------------
# 3. Save the processed dataset with ratios
# --------------------------------------------------

df.to_csv("data/processed/apple_financials_with_ratios.csv", index=False)

print("Processed dataset saved successfully.")
print(df)

# --------------------------------------------------
# 4. Create a visuals folder if it does not exist
# --------------------------------------------------

os.makedirs("visuals", exist_ok=True)

# --------------------------------------------------
# 5. Revenue trend chart
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(df["fiscal_year"], df["revenue"], marker="o")
plt.title("Apple Revenue Trend")
plt.xlabel("Fiscal Year")
plt.ylabel("Revenue ($ millions)")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/revenue_trend.png")
plt.close()

# --------------------------------------------------
# 6. Profitability margin chart
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(df["fiscal_year"], df["gross_margin_pct"], marker="o", label="Gross Margin")
plt.plot(df["fiscal_year"], df["operating_margin_pct"], marker="o", label="Operating Margin")
plt.plot(df["fiscal_year"], df["net_margin_pct"], marker="o", label="Net Margin")
plt.title("Apple Profitability Margin Trend")
plt.xlabel("Fiscal Year")
plt.ylabel("Margin %")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/profitability_margins.png")
plt.close()

# --------------------------------------------------
# 7. Free cash flow trend chart
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(df["fiscal_year"], df["free_cash_flow"], marker="o")
plt.title("Apple Free Cash Flow Trend")
plt.xlabel("Fiscal Year")
plt.ylabel("Free Cash Flow ($ millions)")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/free_cash_flow_trend.png")
plt.close()

# --------------------------------------------------
# 8. Balance sheet chart
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(df["fiscal_year"], df["total_assets"], marker="o", label="Total Assets")
plt.plot(df["fiscal_year"], df["total_liabilities"], marker="o", label="Total Liabilities")
plt.plot(df["fiscal_year"], df["shareholders_equity"], marker="o", label="Shareholders Equity")
plt.title("Apple Balance Sheet Trend")
plt.xlabel("Fiscal Year")
plt.ylabel("$ millions")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/balance_sheet_trend.png")
plt.close()

print("Charts created successfully in the visuals folder.")

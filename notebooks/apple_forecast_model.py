# Apple 3-Year Forecast Model
# Author: Uday Bhaskar Kokkera

import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# 1. Load forecast assumptions
# --------------------------------------------------

assumptions = pd.read_csv("data/processed/apple_forecast_assumptions.csv")

# Apple FY2025 actual revenue, in $ millions
starting_revenue = 416161

forecast_rows = []

# --------------------------------------------------
# 2. Build forecast by scenario
# --------------------------------------------------

for scenario in assumptions["scenario"].unique():
    scenario_df = assumptions[assumptions["scenario"] == scenario].sort_values("forecast_year")
    revenue = starting_revenue

    for _, row in scenario_df.iterrows():
        revenue = revenue * (1 + row["revenue_growth_pct"] / 100)
        gross_profit = revenue * row["gross_margin_pct"] / 100
        operating_income = revenue * row["operating_margin_pct"] / 100
        net_income = revenue * row["net_margin_pct"] / 100
        capital_expenditures = revenue * row["capex_pct_of_revenue"] / 100
        free_cash_flow = revenue * row["fcf_margin_pct"] / 100

        forecast_rows.append({
            "scenario": scenario,
            "forecast_year": int(row["forecast_year"]),
            "revenue": round(revenue, 0),
            "gross_profit": round(gross_profit, 0),
            "operating_income": round(operating_income, 0),
            "net_income": round(net_income, 0),
            "capital_expenditures": round(capital_expenditures, 0),
            "free_cash_flow": round(free_cash_flow, 0),
            "revenue_growth_pct": row["revenue_growth_pct"],
            "gross_margin_pct": row["gross_margin_pct"],
            "operating_margin_pct": row["operating_margin_pct"],
            "net_margin_pct": row["net_margin_pct"],
            "capex_pct_of_revenue": row["capex_pct_of_revenue"],
            "fcf_margin_pct": row["fcf_margin_pct"]
        })

forecast = pd.DataFrame(forecast_rows)

# --------------------------------------------------
# 3. Save forecast output
# --------------------------------------------------

forecast.to_csv("data/processed/apple_forecast_output.csv", index=False)

print("Forecast output saved successfully.")
print(forecast)

# --------------------------------------------------
# 4. Create forecast visuals
# --------------------------------------------------

os.makedirs("visuals", exist_ok=True)

charts = [
    ("revenue", "Apple Revenue Forecast by Scenario", "Revenue ($ millions)", "forecast_revenue_scenarios.png"),
    ("net_income", "Apple Net Income Forecast by Scenario", "Net Income ($ millions)", "forecast_net_income_scenarios.png"),
    ("free_cash_flow", "Apple Free Cash Flow Forecast by Scenario", "Free Cash Flow ($ millions)", "forecast_free_cash_flow_scenarios.png"),
]

for metric, title, ylabel, filename in charts:
    plt.figure(figsize=(8, 5))
    for scenario in forecast["scenario"].unique():
        scenario_data = forecast[forecast["scenario"] == scenario]
        plt.plot(scenario_data["forecast_year"], scenario_data[metric], marker="o", label=scenario)
    plt.title(title)
    plt.xlabel("Forecast Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"visuals/{filename}")
    plt.close()

print("Forecast visuals created successfully.")

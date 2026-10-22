from typing import Any
from unittest import result

import pandas as pd


def get_latest_quarter(
    dataframes: dict[str, pd.DataFrame]
) -> str:
    quarters = dataframes["Regional_Performance"]["Quarter"].unique()
    return sorted(quarters)[-1]


def calculate_kpis(
    dataframes: dict[str, pd.DataFrame]
) -> dict[str, Any]:

    performance = dataframes["Regional_Performance"].copy()
    customer = dataframes["Customer_Experience"].copy()

    quarters = sorted(performance["Quarter"].unique())

    latest_quarter = quarters[-1]
    previous_quarter = quarters[-2]

    latest_performance = performance[
        performance["Quarter"] == latest_quarter
    ].copy()

    previous_performance = performance[
        performance["Quarter"] == previous_quarter
    ].copy()

    latest_customer = customer[
        customer["Quarter"] == latest_quarter
    ].copy()

    total_revenue = latest_performance["Revenue_USD_M"].sum()
    previous_revenue = previous_performance["Revenue_USD_M"].sum()

    revenue_growth_qoq = (
        (total_revenue - previous_revenue)
        / previous_revenue
        * 100
    )

    customer_with_units = latest_customer.merge(
        latest_performance[["Region", "Units_Sold_K"]],
        on="Region",
        how="left",
    )

    weighted_nps = (
        customer_with_units["NPS"]
        * customer_with_units["Units_Sold_K"]
    ).sum() / customer_with_units["Units_Sold_K"].sum()

    result = {
        "latest_quarter": latest_quarter,
        "previous_quarter": previous_quarter,
        "total_revenue_usd_m": total_revenue,
        "qoq_revenue_growth_pct": revenue_growth_qoq,
        "weighted_nps": weighted_nps,
    }
    return result

def analyze_regional_performance(
    performance: pd.DataFrame,
) -> dict[str, Any]:

    quarters = sorted(performance["Quarter"].unique())
    first_quarter = quarters[0]
    latest_quarter = quarters[-1]

    first = performance[
        performance["Quarter"] == first_quarter
    ][["Region", "Revenue_USD_M"]].rename(
        columns={"Revenue_USD_M": "First_Revenue"}
    )

    latest = performance[
        performance["Quarter"] == latest_quarter
    ].copy()

    comparison = latest.merge(first, on="Region")

    comparison["Revenue_Change_pct"] = (
        (
            comparison["Revenue_USD_M"]
            - comparison["First_Revenue"]
        )
        / comparison["First_Revenue"]
        * 100
    )

    strongest_growth = comparison.loc[
        comparison["Revenue_Change_pct"].idxmax()
    ]

    weakest_growth = comparison.loc[
        comparison["Revenue_Change_pct"].idxmin()
    ]

    highest_returns = comparison.loc[
        comparison["Returns_Rate_pct"].idxmax()
    ]

    return {
        "comparison": comparison,
        "strongest_growth_region": strongest_growth["Region"],
        "strongest_growth_pct": strongest_growth["Revenue_Change_pct"],
        "weakest_growth_region": weakest_growth["Region"],
        "weakest_growth_pct": weakest_growth["Revenue_Change_pct"],
        "highest_returns_region": highest_returns["Region"],
        "highest_returns_pct": highest_returns["Returns_Rate_pct"],
    }
 
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = Path("output/charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REGION_COLORS = {
    "North America": "#1F4E78",
    "Europe": "#5B9BD5",
    "APAC": "#70AD47",
    "Latin America": "#C00000",
}


def create_performance_chart(
    performance: pd.DataFrame,
) -> Path:

    pivot = performance.pivot(
        index="Quarter",
        columns="Region",
        values="Revenue_USD_M",
    )

    region_order = [
        "North America",
        "Europe",
        "APAC",
        "Latin America",
    ]

    pivot = pivot[region_order]

    axis = pivot.plot(
        kind="bar",
        figsize=(10, 5.5),
        color=[REGION_COLORS[region] for region in region_order],
        width=0.78,
    )

    axis.set_title(
        "Quarterly Revenue by Region",
        fontsize=16,
        fontweight="bold",
        loc="left",
    )
    axis.set_xlabel("")
    axis.set_ylabel("Revenue (USD millions)")
    axis.tick_params(axis="x", rotation=0)
    axis.grid(axis="y", alpha=0.20)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

    axis.legend(
        title="",
        frameon=False,
        ncol=4,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.12),
    )

    plt.tight_layout()

    output_path = OUTPUT_DIR / "performance_chart.png"

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight",
        transparent=True,
    )
    plt.close()

    return output_path
def create_customer_chart(
    customer: pd.DataFrame,
) -> Path:

    pivot = customer.pivot(
        index="Quarter",
        columns="Region",
        values="NPS",
    )

    region_order = [
        "North America",
        "Europe",
        "APAC",
        "Latin America",
    ]

    pivot = pivot[region_order]

    figure, axis = plt.subplots(figsize=(10, 5.5))

    for region in region_order:
        axis.plot(
            pivot.index,
            pivot[region],
            marker="o",
            linewidth=2.5,
            markersize=6,
            label=region,
            color=REGION_COLORS[region],
        )

    axis.set_title(
        "Customer NPS Trend by Region",
        fontsize=16,
        fontweight="bold",
        loc="left",
    )
    axis.set_xlabel("")
    axis.set_ylabel("NPS")
    axis.grid(axis="y", alpha=0.20)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

    axis.legend(
        title="",
        frameon=False,
        ncol=4,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.12),
    )

    plt.tight_layout()

    output_path = OUTPUT_DIR / "customer_chart.png"

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight",
        transparent=True,
    )
    plt.close()

    return output_path
def create_risk_chart(
    risk: pd.DataFrame,
) -> Path:

    latest_quarter = sorted(risk["Quarter"].unique())[-1]

    latest = risk[
        risk["Quarter"] == latest_quarter
    ].sort_values(
        "Stockout_Rate_pct",
        ascending=True,
    )

    colors = [
        REGION_COLORS[region]
        for region in latest["Region"]
    ]

    figure, axis = plt.subplots(figsize=(10, 5.5))

    bars = axis.barh(
        latest["Region"],
        latest["Stockout_Rate_pct"],
        color=colors,
    )

    axis.set_title(
        f"Stockout Rate by Region | {latest_quarter}",
        fontsize=16,
        fontweight="bold",
        loc="left",
    )
    axis.set_xlabel("Stockout rate (%)")
    axis.set_ylabel("")
    axis.grid(axis="x", alpha=0.20)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.spines["left"].set_visible(False)

    axis.bar_label(
        bars,
        labels=[
            f"{value:.1f}%"
            for value in latest["Stockout_Rate_pct"]
        ],
        padding=4,
    )

    plt.tight_layout()

    output_path = OUTPUT_DIR / "risk_chart.png"

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight",
        transparent=True,
    )
    plt.close()

    return output_path
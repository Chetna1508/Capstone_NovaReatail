import pandas as pd


EXPECTED_COLUMNS = {
    "Regional_Performance": {
        "Quarter",
        "Region",
        "Revenue_USD_M",
        "Units_Sold_K",
        "Returns_Rate_pct",
        "Marketing_Spend_USD_M",
    },
    "Customer_Experience": {
        "Quarter",
        "Region",
        "NPS",
        "CSAT_pct",
        "Avg_Delivery_Days",
        "Support_Tickets_K",
    },
    "Operational_Risk": {
        "Quarter",
        "Region",
        "Stockout_Rate_pct",
        "Return_Processing_Days",
        "Warehouse_Capacity_Util_pct",
        "Fraud_Incidents",
    },
}


def validate_data(dataframes: dict[str, pd.DataFrame]) -> None:
    missing_sheets = set(EXPECTED_COLUMNS) - set(dataframes)

    if missing_sheets:
        raise ValueError(f"Missing required worksheets: {missing_sheets}")

    for sheet_name, expected_columns in EXPECTED_COLUMNS.items():
        dataframe = dataframes[sheet_name]

        missing_columns = expected_columns - set(dataframe.columns)

        if missing_columns:
            raise ValueError(
                f"{sheet_name} is missing columns: {missing_columns}"
            )

        if dataframe.empty:
            raise ValueError(f"{sheet_name} contains no data.")

        if dataframe[list(expected_columns)].isna().any().any():
            raise ValueError(
                f"{sheet_name} contains missing values in required columns."
            )

        duplicated_rows = dataframe.duplicated(
            subset=["Quarter", "Region"]
        ).sum()

        if duplicated_rows:
            raise ValueError(
                f"{sheet_name} has {duplicated_rows} duplicated "
                f"Quarter-Region rows."
            )

    print("Dataset structure is valid.")
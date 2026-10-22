from pathlib import Path

import pandas as pd


# ============================================================
# PATH CONFIGURATION
# ============================================================

# Current file:
# Master_Folder/NovaRetail/NovaRetail/src/data_loader.py

# Inner NovaRetail application folder
APP_DIR = Path(__file__).resolve().parent.parent

# Outer NovaRetail project folder
PROJECT_ROOT = APP_DIR.parent

# Assets folder
ASSETS_DIR = PROJECT_ROOT / "assets"

# Dataset location
DATASET_PATH = ASSETS_DIR / "novaretail_dataset.xlsx"


# ============================================================
# LOAD DATA
# ============================================================

def load_data(
    workbook_path: Path = DATASET_PATH
) -> dict[str, pd.DataFrame]:

    workbook_path = Path(workbook_path)

    if not workbook_path.exists():
        raise FileNotFoundError(
            "\nDataset not found.\n"
            f"Expected location:\n{workbook_path}\n"
        )

    print(f"\nLoading dataset from:\n{workbook_path}")

    dataframes = pd.read_excel(
        workbook_path,
        sheet_name=None,
        engine="openpyxl",
    )

    return dataframes


# ============================================================
# INSPECT DATA
# ============================================================

def inspect_data(
    dataframes: dict[str, pd.DataFrame]
) -> None:

    for sheet_name, dataframe in dataframes.items():

        print("\n" + "=" * 80)
        print(f"SHEET: {sheet_name}")
        print("=" * 80)

        print(f"Rows: {len(dataframe)}")
        print(f"Columns: {dataframe.columns.tolist()}")

        print("\nData types:")
        print(dataframe.dtypes)

        print("\nMissing values:")
        print(dataframe.isna().sum())

        print("\nSample:")
        print(dataframe.head())


# ============================================================
# TEST DATA LOADER
# ============================================================

if __name__ == "__main__":

    print("\n======================================")
    print("NOVARETAIL DATA LOADER TEST")
    print("======================================")

    print(f"\nApplication directory:\n{APP_DIR}")

    print(f"\nProject root:\n{PROJECT_ROOT}")

    print(f"\nAssets directory:\n{ASSETS_DIR}")

    print(f"\nLooking for dataset:\n{DATASET_PATH}")

    print(f"\nDataset exists: {DATASET_PATH.exists()}")

    data = load_data()

    print("\nDataset loaded successfully.")

    print(f"Sheets found: {list(data.keys())}")

    inspect_data(data)
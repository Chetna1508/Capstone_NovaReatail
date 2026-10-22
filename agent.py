from pathlib import Path
from zipfile import ZipFile, BadZipFile


# ============================================================
# PATHS
# ============================================================

# agent.py:
# Master_Folder/NovaRetail/NovaRetail/agent.py

APP_DIR = Path(__file__).resolve().parent

# Outer NovaRetail folder
PROJECT_ROOT = APP_DIR.parent

# Existing icons are here:
# Master_Folder/NovaRetail/assets/icons
ICON_DIR = PROJECT_ROOT / "assets" / "icons"

# Optional ZIP location
ICON_ZIP = PROJECT_ROOT / "novaretail_icon_repo.zip"


# ============================================================
# ICON SETUP
# ============================================================

def setup_icons():

    print("\n======================================")
    print("NovaRetail Icon Setup")
    print("======================================")

    # --------------------------------------------------------
    # Check whether icons already exist
    # --------------------------------------------------------

    if ICON_DIR.exists():

        existing_icons = list(ICON_DIR.glob("*.png"))

        if existing_icons:

            print("\nIcons already exist.")
            print(f"\nIcon directory:\n{ICON_DIR}")

            print("\nAvailable icons:")

            for icon in existing_icons:
                print(f"  - {icon.name}")

            print("\nNo ZIP extraction is required.")

            return

    # --------------------------------------------------------
    # If icons do not exist, check for ZIP
    # --------------------------------------------------------

    if not ICON_ZIP.exists():

        raise FileNotFoundError(
            "\nIcons were not found and the icon ZIP "
            "was also not found.\n\n"
            f"Expected icon directory:\n{ICON_DIR}\n\n"
            f"Expected ZIP:\n{ICON_ZIP}\n"
        )

    # --------------------------------------------------------
    # Create icon directory
    # --------------------------------------------------------

    ICON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Extract ZIP
    # --------------------------------------------------------

    try:

        print(f"\nExtracting:\n{ICON_ZIP}")

        with ZipFile(ICON_ZIP, "r") as zip_file:
            zip_file.extractall(ICON_DIR)

    except BadZipFile:

        raise ValueError(
            f"\nInvalid ZIP file:\n{ICON_ZIP}"
        )

    print("\nIcons extracted successfully.")
    print(f"\nIcon directory:\n{ICON_DIR}")


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    setup_icons()
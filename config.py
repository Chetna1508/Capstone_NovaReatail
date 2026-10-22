from pathlib import Path


# Inner application folder
# ...\Master_Folder\NovaRetail\NovaRetail
APP_DIR = Path(__file__).resolve().parent.parent

# Outer project folder
# ...\Master_Folder\NovaRetail
PROJECT_ROOT = APP_DIR.parent


# ============================================================
# ASSETS
# ============================================================

ASSETS_DIR = PROJECT_ROOT / "assets"

DATASET_PATH = ASSETS_DIR / "novaretail_dataset.xlsx"

TEMPLATE_PATH = ASSETS_DIR / "novaretail_template.pptx"

ICON_DIR = ASSETS_DIR / "icons"


# ============================================================
# OUTPUT
# ============================================================

OUTPUT_DIR = APP_DIR / "output"

OUTPUT_PPTX = OUTPUT_DIR / "NovaRetail_Q2_2026_QBR.pptx"


# ============================================================
# ICONS
# ============================================================

ICON_MAPPING = {
    1: ICON_DIR / "growth_chart.png",
    2: ICON_DIR / "globe_region.png",
    3: ICON_DIR / "customer_star.png",
    4: ICON_DIR / "risk_alert.png",
    5: ICON_DIR / "lightbulb_action.png",
}
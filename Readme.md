NovaRetail Executive Deck Automation
Overview
This project analyzes NovaRetail quarterly business data and programmatically generates a five-slide executive PowerPoint presentation using Python.

Capabilities
Reads data from a multi-sheet Excel workbook
Calculates executive KPIs
Identifies positive and negative regional trends
Generates performance, customer and risk charts
Locates PowerPoint placeholders using shape names
Replaces placeholder text, charts and icons
Preserves the supplied PowerPoint layout
Produces a presentation ready for leadership review
Project Structure
assets/: Input dataset, template and icons
src/: Analysis and presentation-generation modules
output/: Generated charts and PowerPoint presentation
main.py: Main workflow entry point
Setup
python -m venv nova_venv
nova_venv\Scripts\activate
pip install -r requirements.txt
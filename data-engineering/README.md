# Fire Data Analysis & Visualization

This project performs an in-depth analysis of fire incident data using Python. The goal is to understand fire intensity, distribution, and trends across different locations and time periods.

---

## Project Overview

Wildfire monitoring is critical for environmental safety and disaster management. This analysis focuses on:

- Fire intensity using **Brightness** and **Fire Radiative Power (FRP)**
- Location-based fire activity comparison
- Confidence level distribution of fire detections
- Time-based trends in fire intensity

---

## Project Structure
data-engineering/
│
├── analysis.py # Data analysis & visualization
│
├── pipelines/ # Data engineering pipelines
│ ├── extract.py # Data ingestion script
│ ├── transform.py # Data cleaning & transformation
│ ├── load_data.py # Load processed data
  ├── validation.py # validate processed data
  ├── save_to_db.py # Save data in form of tables in postgresql database
  ├── main.py # main script
│
├── data/
│ ├── raw/ # Raw input data
│ │ └── fire_data.csv
│ └── processed/ # Cleaned/processed data
│ └── fact_fire.csv
  └── dim_date.csv
  └── dim_location.csv

│
├── outputs/ # Generated visualizations
│ ├── brightness_vs_frp.png
│ ├── location_analysis.png
│ ├── confidence_distribution.png
│ └── time_trend.png
│
└── README.md

---

## Technologies Used

- Python 
- Pandas (data processing)
- Matplotlib (data visualization)

---

## How to Run the Project

### 1. Navigate to project directory

```bash
cd data-engineering

2. Install required libraries
pip install pandas matplotlib
3. Run the analysis
python3 analysis.py

Analysis & Results
1. Fire Intensity (Brightness vs FRP)

Insight:

Higher brightness values generally correspond to higher FRP.
Indicates stronger and more intense fire events.
2. Location-Based Analysis

Insight:

Certain locations consistently show higher fire intensity.
Useful for identifying high-risk regions.
3. Confidence Distribution

Insight:

Most fire detections fall within mid-to-high confidence levels.
High-confidence detections are more reliable for analysis.
4. Fire Trend Over Time

Insight:

Helps track whether fire intensity is increasing or decreasing over time.
Useful for trend monitoring and forecasting.
Key Learnings
Fire intensity can be effectively analyzed using Brightness and FRP
Data visualization helps uncover hidden patterns
Location-based grouping provides actionable insights
Time-series analysis helps identify trends
Contribution Guidelines

This project follows a structured collaboration workflow:

No direct pushes to main

Use feature branches:

feature/fire-analysis-visualization
Submit all changes via Pull Requests (PRs)
At least one approval required before merging
Git Workflow
# Create a new branch
git checkout -b feature/fire-analysis-visualization

# Add changes
git add .

# Commit changes
git commit -m "feat: add fire data analysis and visualizations"

# Push to your fork
git push origin feature/fire-analysis-visualization

Then open a Pull Request on GitHub.

Future Improvements
Add machine learning model for fire prediction
Advanced visualizations (heatmaps, correlations)
Integration with real-time satellite data
Automated report generation (PDF)

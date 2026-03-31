import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load Data
# -----------------------------
def load_data(file_path):
    print("Loading data...")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")

    df = pd.read_csv(file_path)
    print("Data loaded successfully\n")
    return df


# -----------------------------
# Validate Data
# -----------------------------
def validate_data(df):
    print("Validating data...")

    required_columns = ['date_id', 'location_id', 'brightness', 'confidence', 'frp']

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    print("Data validation passed\n")


# -----------------------------
# Create Output Folder
# -----------------------------
def create_output_folder():
    if not os.path.exists("outputs"):
        os.makedirs("outputs")


# -----------------------------
# Basic Statistics
# -----------------------------
def basic_stats(df):
    print("Basic Statistics:")
    print(df.describe())
    print("\n")


# -----------------------------
# Fire Intensity Analysis
# -----------------------------
def analyze_intensity(df):
    print("Fire Intensity Analysis:")

    top_fires = df.sort_values(by='brightness', ascending=False).head(5)
    print("\nTop 5 Most Intense Fires (Brightness):")
    print(top_fires)

    top_frp = df.sort_values(by='frp', ascending=False).head(5)
    print("\nTop 5 Highest FRP Fires:")
    print(top_frp)

    # Plot
    plt.figure()
    plt.scatter(df['brightness'], df['frp'])
    plt.xlabel("Brightness")
    plt.ylabel("FRP")
    plt.title("Brightness vs FRP")
    plt.grid()

    plt.savefig("outputs/brightness_vs_frp.png")
    plt.close()

    print("Saved: outputs/brightness_vs_frp.png")

    # Insight
    print("\nInsight: Higher brightness generally corresponds to higher FRP, indicating stronger fires.\n")


# -----------------------------
# Location Analysis
# -----------------------------
def location_analysis(df):
    print("Location-Based Analysis:")

    location_summary = df.groupby('location_id').agg({
        'brightness': 'mean',
        'confidence': 'mean',
        'frp': 'mean'
    }).reset_index()

    print(location_summary)

    # Plot
    plt.figure()
    plt.bar(location_summary['location_id'], location_summary['frp'])
    plt.xlabel("Location ID")
    plt.ylabel("Average FRP")
    plt.title("Average Fire Intensity per Location")
    plt.grid()

    plt.savefig("outputs/location_analysis.png")
    plt.close()

    print("Saved: outputs/location_analysis.png")

    print("\nInsight: Some locations show consistently higher fire intensity.\n")


# -----------------------------
# Confidence Analysis
# -----------------------------
def confidence_analysis(df):
    print("Confidence Analysis:")

    high_conf = df[df['confidence'] > 80]
    print("\nHigh Confidence Fires (>80):")
    print(high_conf)

    plt.figure()
    plt.hist(df['confidence'], bins=10)
    plt.xlabel("Confidence")
    plt.ylabel("Frequency")
    plt.title("Confidence Distribution")
    plt.grid()

    plt.savefig("outputs/confidence_distribution.png")
    plt.close()

    print("Saved: outputs/confidence_distribution.png")

    print("\nInsight: Majority of detections fall in mid-to-high confidence range.\n")


# -----------------------------
# Date Analysis
# -----------------------------
def date_analysis(df):
    print("Date-Based Analysis:")

    date_summary = df.groupby('date_id').agg({
        'brightness': 'mean',
        'confidence': 'mean',
        'frp': 'mean'
    }).reset_index()

    print(date_summary)

    plt.figure()
    plt.plot(date_summary['date_id'], date_summary['frp'], marker='o')
    plt.xlabel("Date ID")
    plt.ylabel("Average FRP")
    plt.title("Fire Intensity Trend Over Time")
    plt.grid()

    plt.savefig("outputs/time_trend.png")
    plt.close()

    print("Saved: outputs/time_trend.png")

    print("\nInsight: Fire intensity trend over time can indicate increasing or decreasing severity.\n")


# -----------------------------
# Main Function
# -----------------------------
def main():
    create_output_folder()

    df = load_data("data/processed/fact_fire.csv")

    validate_data(df)

    basic_stats(df)
    analyze_intensity(df)
    location_analysis(df)
    confidence_analysis(df)
    date_analysis(df)

    print("\nANALYSIS COMPLETE!")


# Run script
if __name__ == "__main__":
    main()
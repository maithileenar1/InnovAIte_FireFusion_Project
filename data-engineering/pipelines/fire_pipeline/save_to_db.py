import os
import pandas as pd
import logging
from sqlalchemy import create_engine

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------- VALIDATION FUNCTION ----------------
def validate_dataframe(df, name):

    logging.info(f"Validating {name}...")

    # Check missing values
    if df.isnull().sum().sum() > 0:
        raise ValueError(f"Missing values found in {name}")

    # Example validations (customize based on your schema)
    if 'latitude' in df.columns:
        if not df['latitude'].between(-90, 90).all():
            raise ValueError(f"Invalid latitude in {name}")

    if 'longitude' in df.columns:
        if not df['longitude'].between(-180, 180).all():
            raise ValueError(f"Invalid longitude in {name}")

    logging.info(f"{name} validation passed")


# ---------------- MAIN FUNCTION ----------------
def save_to_database():

    try:
        # PostgreSQL credentials
        username = "postgres"
        password = "pitam"
        host = "localhost"
        port = "5432"
        db_name = "firefusion"

        logging.info("Pipeline started!!")

        # Create DB connection
        engine = create_engine(
            f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
        )

        # Path handling
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        processed_path = os.path.join(base_dir, "data", "processed")

        logging.info(f"Loading data from {processed_path}")

        # Load CSV files
        dim_date = pd.read_csv(os.path.join(processed_path, "dim_date.csv"))
        dim_location = pd.read_csv(os.path.join(processed_path, "dim_location.csv"))
        fact_fire = pd.read_csv(os.path.join(processed_path, "fact_fire.csv"))

        logging.info("CSV files loaded")

        # 🔍 VALIDATION STEP
        validate_dataframe(dim_date, "dim_date")
        validate_dataframe(dim_location, "dim_location")
        validate_dataframe(fact_fire, "fact_fire")

        # SAVE TO DATABASE
        logging.info("Saving data to PostgreSQL...")

        dim_date.to_sql("dim_date", engine, if_exists="append", index=False)
        dim_location.to_sql("dim_location", engine, if_exists="append", index=False)
        fact_fire.to_sql("fact_fire", engine, if_exists="append", index=False)

        logging.info("Data successfully stored in PostgreSQL")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise


# ---------------- RUN SCRIPT ----------------
if __name__ == "__main__":
    save_to_database()
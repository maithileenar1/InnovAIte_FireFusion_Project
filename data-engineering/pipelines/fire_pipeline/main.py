import logging

from extract import load_fire_data
from transform import clean_fire_data, create_star_schema
from load import save_data
from validation import validate_data

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def run_pipeline():

    try:
        logging.info("🚀 Pipeline started")

        # ---------------- EXTRACT ----------------
        print("Loading data...")
        df = load_fire_data()
        logging.info(f"Data loaded: {df.shape}")

        # ---------------- TRANSFORM ----------------
        print("Cleaning data...")
        df_clean = clean_fire_data(df)
        logging.info(f"Data cleaned: {df_clean.shape}")

        # ---------------- VALIDATION ----------------
        print("Validating data...")
        validate_data(df_clean)
        logging.info("Data validation passed")

        # ---------------- STAR SCHEMA ----------------
        print("Creating star schema...")
        dim_date, dim_location, fact_fire = create_star_schema(df_clean)
        logging.info("Star schema created")

        # ---------------- LOAD TO DATABASE ----------------
        print("Saving to PostgreSQL...")

        save_data(dim_date, dim_location, fact_fire)

        logging.info("Data successfully saved to PostgreSQL")
        print("Data successfully saved to PostgreSQL!")

        logging.info("Pipeline completed successfully")
        print("Pipeline completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        print(f"Error: {str(e)}")
        raise


if __name__ == "__main__":
    run_pipeline()
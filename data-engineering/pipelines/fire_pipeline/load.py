import os

import logging
import pandas as pd
from sqlalchemy import create_engine

def save_data(dim_date, dim_location, fact_fire):

    username = "postgres"
    password = "pitam"
    host = "localhost"
    port = "5432"
    db_name = "firefusion"

    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
    )

    logging.info("Saving data to PostgreSQL...")

    dim_date.to_sql("dim_date", engine, if_exists="append", index=False)
    dim_location.to_sql("dim_location", engine, if_exists="append", index=False)
    fact_fire.to_sql("fact_fire", engine, if_exists="append", index=False)

    logging.info("Data successfully saved to PostgreSQL!")
    print("Data successfully saved to PostgreSQL!")
import logging

def save_data(dim_date, dim_location, fact_fire):

    # Example: save to PostgreSQL (already written earlier)
    dim_date.to_sql("dim_date", engine, if_exists="append", index=False)
    dim_location.to_sql("dim_location", engine, if_exists="append", index=False)
    fact_fire.to_sql("fact_fire", engine, if_exists="append", index=False)

    print("Data successfully saved to PostgreSQL!")
    logging.info("Data successfully saved to PostgreSQL!")
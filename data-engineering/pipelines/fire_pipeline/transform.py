import pandas as pd

def clean_fire_data(df):

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (basic)
    df = df.dropna(subset=['latitude', 'longitude', 'acq_date'])

    # Convert date column (FIXED)
    df['acq_date'] = pd.to_datetime(df['acq_date'])

    return df

def create_star_schema(df):

    # ---- DIM DATE ----
    dim_date = df[['acq_date']].drop_duplicates().copy()
    dim_date['date_id'] = dim_date.index

    dim_date['year'] = dim_date['acq_date'].dt.year
    dim_date['month'] = dim_date['acq_date'].dt.month
    dim_date['day'] = dim_date['acq_date'].dt.day

    # ---- DIM LOCATION ----
    dim_location = df[['latitude', 'longitude']].drop_duplicates().copy()
    dim_location['location_id'] = dim_location.index

    # ---- FACT TABLE ----
    fact_fire = df.copy()

    fact_fire = fact_fire.merge(dim_date, on='acq_date')
    fact_fire = fact_fire.merge(dim_location, on=['latitude', 'longitude'])

    fact_fire = fact_fire[['date_id', 'location_id', 'brightness', 'confidence', 'frp']]

    return dim_date, dim_location, fact_fire
def validate_data(df):

    if df.isnull().sum().sum() > 0:
        raise ValueError("Missing values found")

    if not (df['latitude'].between(-90, 90)).all():
        raise ValueError("Invalid latitude values")

    if not (df['longitude'].between(-180, 180)).all():
        raise ValueError("Invalid longitude values")

    print("Data validation passed")
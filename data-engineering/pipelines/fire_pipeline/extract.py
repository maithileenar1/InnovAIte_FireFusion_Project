import pandas as pd
import os

def load_fire_data():

    # Get project root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    file_path = os.path.join(base_dir, "data", "raw", "fire_data.csv")

    print("Looking for file at:", file_path)

    df = pd.read_csv(file_path)

    print("Data Loaded Successfully")
    return df
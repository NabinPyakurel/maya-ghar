# src/data_preprocessing.py
import pandas as pd
import numpy as np

def load_and_clean(path="data/raw/World_Development_Indicators.csv"):
    """
    Load and clean the World Development Indicators dataset.
    """
    df = pd.read_csv(path)

    # Drop completely empty rows
    df_clean = df.dropna(how="all")

    # Convert from wide to long format
    df_long = df_clean.melt(
        id_vars=['Country Name', 'Country Code', 'Series Name', 'Series Code'],
        var_name='Year', value_name='Value'
    )

    # Extract year as integer
    df_long['Year'] = df_long['Year'].astype(str).str.extract(r'(\d{4})').astype(float)
    df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')

    # Convert Value to numeric
    df_long['Value'] = pd.to_numeric(df_long['Value'], errors='coerce')

    return df_long

def filter_series(df, series_code, rename_col):
    """
    Filter dataset by Series Code and rename Value column.
    """
    sub_df = df[df['Series Code'] == series_code].copy()
    sub_df = sub_df.rename(columns={'Value': rename_col})
    return sub_df

def merge_series(df1, df2, on=['Country Name','Country Code','Year']):
    """
    Merge two filtered series into one dataframe.
    """
    return df1.merge(df2, on=on)

def save_processed(df, outpath="data/processed/merged_df.csv"):
    """
    Save dataframe to CSV.
    """
    df.to_csv(outpath, index=False)
    print(f"✅ Saved processed dataset to {outpath}")

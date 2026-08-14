"""
Day 92: Data Cleaning with Pandas
Requires: pip install pandas
"""

import numpy as np
import pandas as pd


def build_messy_dataframe():
    data = {
        "name": ["  Ali ", "SARA", "zain", "Ali", None],
        "age": [25, np.nan, 22, 25, 40],
        "city": ["lahore", "Karachi", "ISLAMABAD", "lahore", "Multan"],
        "signup_date": ["2024-01-05", "2024-02-10", "2024-03-15", "2024-01-05", "2024-04-01"],
    }
    return pd.DataFrame(data)


def show_missing(df):
    print("--- Missing Values ---")
    print(df.isnull().sum())


def clean_missing(df):
    print("\n--- Handling Missing Values ---")
    df = df.dropna(subset=["name"])  # can't work with a nameless row
    df["age"] = df["age"].fillna(df["age"].mean())
    print(df)
    return df


def remove_duplicates(df):
    print("\n--- Removing Duplicates ---")
    print("Duplicate rows:\n", df[df.duplicated()])
    df = df.drop_duplicates()
    print("After dropping duplicates:\n", df)
    return df


def fix_types_and_text(df):
    print("\n--- Fixing Types & Text ---")
    df["name"] = df["name"].str.strip().str.title()
    df["city"] = df["city"].str.title()
    df["age"] = df["age"].astype(int)
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    print(df)
    print("\nDtypes:\n", df.dtypes)
    return df


def add_derived_column(df):
    print("\n--- Derived Column ---")
    df["age_group"] = df["age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
    print(df)
    return df


if __name__ == "__main__":
    df = build_messy_dataframe()
    print("Original (messy) data:\n", df, "\n")

    show_missing(df)
    df = clean_missing(df)
    df = remove_duplicates(df)
    df = fix_types_and_text(df)
    df = add_derived_column(df)

    print("\n--- Final Clean DataFrame ---")
    print(df)

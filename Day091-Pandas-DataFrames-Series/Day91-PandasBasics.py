"""
Day 91: Pandas DataFrames & Series
Requires: pip install pandas
"""

import pandas as pd


def series_demo():
    print("--- Series ---")
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print(s)
    print("Value at 'b':", s["b"])


def dataframe_demo():
    print("\n--- DataFrame ---")
    data = {
        "name": ["Ali", "Sara", "Zain", "Hina"],
        "age": [25, 30, 22, 28],
        "city": ["Lahore", "Karachi", "Islamabad", "Lahore"],
    }
    df = pd.DataFrame(data)
    print(df)
    return df


def exploring_demo(df: pd.DataFrame):
    print("\n--- Exploring ---")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("\nDescribe:\n", df.describe())


def selecting_demo(df: pd.DataFrame):
    print("\n--- Selecting & Filtering ---")
    print("Names only:\n", df["name"])
    print("\nAdults over 25:\n", df[df["age"] > 25])


def modifying_demo(df: pd.DataFrame):
    print("\n--- Adding Columns ---")
    df["is_adult"] = df["age"] >= 18
    print(df)


def grouping_demo(df: pd.DataFrame):
    print("\n--- Grouping ---")
    print("Average age by city:\n", df.groupby("city")["age"].mean())


if __name__ == "__main__":
    series_demo()
    df = dataframe_demo()
    exploring_demo(df)
    selecting_demo(df)
    modifying_demo(df)
    grouping_demo(df)

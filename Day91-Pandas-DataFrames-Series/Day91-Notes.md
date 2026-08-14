# Day 91: Pandas DataFrames & Series

## What is Pandas?
Pandas is the go-to library for working with tabular (spreadsheet-like)
data in Python. It's built on top of NumPy (Day 90) and provides two main
data structures: **Series** (1D) and **DataFrame** (2D).

## Setup
```bash
pip install pandas
```

## Series — a labeled 1D array
```python
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["b"])   # 20
```

## DataFrame — a labeled 2D table
```python
data = {
    "name": ["Ali", "Sara", "Zain"],
    "age": [25, 30, 22],
    "city": ["Lahore", "Karachi", "Islamabad"],
}
df = pd.DataFrame(data)
print(df)
```

## Reading Data from Files
```python
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")
```

## Exploring a DataFrame
```python
df.head()        # first 5 rows
df.tail(3)        # last 3 rows
df.info()          # column types & non-null counts
df.describe()       # statistical summary of numeric columns
df.columns          # list of column names
df.shape             # (rows, columns)
```

## Selecting Data
```python
df["name"]                # single column -> Series
df[["name", "age"]]       # multiple columns -> DataFrame
df.loc[0]                 # row by label
df.iloc[0]                # row by position
df[df["age"] > 25]        # filter rows by condition
```

## Adding & Modifying Columns
```python
df["is_adult"] = df["age"] >= 18
df["age"] = df["age"] + 1
```

## Sorting & Grouping
```python
df.sort_values("age", ascending=False)
df.groupby("city")["age"].mean()
```

## Summary
Series = one labeled column; DataFrame = a full labeled table (rows +
columns). Pandas makes loading, filtering, and summarizing real-world
tabular data dramatically easier than plain Python lists/dicts.

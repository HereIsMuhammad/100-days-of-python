# Day 92: Data Cleaning with Pandas

## Why Clean Data?
Real-world data is messy: missing values, duplicates, wrong types,
inconsistent formatting. "Garbage in, garbage out" — clean data is
essential before any analysis.

## Finding Missing Values
```python
df.isnull()             # boolean mask, True where value is missing
df.isnull().sum()       # count of missing values per column
df.isnull().sum().sum() # total missing values
```

## Handling Missing Values
```python
df.dropna()                     # drop rows with ANY missing value
df.dropna(subset=["age"])       # drop rows missing a specific column
df.fillna(0)                    # fill missing values with 0
df["age"].fillna(df["age"].mean(), inplace=True)  # fill with column mean
```

## Removing Duplicates
```python
df.duplicated()          # boolean mask of duplicate rows
df.drop_duplicates()     # remove them
```

## Fixing Data Types
```python
df["age"] = df["age"].astype(int)
df["signup_date"] = pd.to_datetime(df["signup_date"])
```

## String Cleaning
```python
df["name"] = df["name"].str.strip()          # remove whitespace
df["name"] = df["name"].str.lower()          # lowercase
df["city"] = df["city"].str.replace("Lhr", "Lahore")
```

## Renaming Columns
```python
df.rename(columns={"nm": "name", "yrs": "age"}, inplace=True)
```

## Detecting Outliers (basic approach)
```python
q1 = df["price"].quantile(0.25)
q3 = df["price"].quantile(0.75)
iqr = q3 - q1
outliers = df[(df["price"] < q1 - 1.5 * iqr) | (df["price"] > q3 + 1.5 * iqr)]
```

## Applying Custom Logic
```python
df["age_group"] = df["age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
```

## Summary
Cleaning is usually 60-80% of any real data project. Pandas gives you a
consistent toolkit — handle missing values, fix types, remove duplicates,
and standardize text — before moving on to analysis or visualization.

# Day 93: Data Visualization (Matplotlib & Seaborn)

## Why Visualize?
Charts reveal patterns, trends, and outliers that are hard to spot in raw
numbers. "A picture is worth a thousand rows."

## Setup
```bash
pip install matplotlib seaborn
```

## Matplotlib Basics
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("chart.png")   # or plt.show() in a local/interactive environment
```

## Common Chart Types
```python
plt.plot(x, y)                       # line chart — trends over time
plt.bar(categories, values)          # bar chart — comparing categories
plt.scatter(x, y)                    # scatter plot — relationship between 2 vars
plt.hist(data, bins=10)              # histogram — distribution of one variable
plt.pie(sizes, labels=labels)        # pie chart — proportions of a whole
```

## Multiple Plots (Subplots)
```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, y)
axes[0].set_title("Line Chart")
axes[1].bar(categories, values)
axes[1].set_title("Bar Chart")
plt.tight_layout()
```

## Seaborn — Built on Matplotlib, Nicer Defaults
Works great directly with Pandas DataFrames.
```python
import seaborn as sns

sns.barplot(data=df, x="city", y="age")
sns.histplot(data=df, x="age", bins=10)
sns.scatterplot(data=df, x="age", y="salary", hue="city")
sns.boxplot(data=df, x="city", y="salary")     # great for spotting outliers
sns.heatmap(df.corr(), annot=True)              # correlation between numeric columns
```

## Styling Tips
```python
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
plt.title("Average Salary by City", fontsize=14)
```

## Matplotlib vs Seaborn
| | Matplotlib | Seaborn |
|---|---|---|
| Control | Very fine-grained | Higher-level, less code |
| Default style | Basic | Attractive, statistical |
| Works well with DataFrames | Needs manual mapping | Native support |

## Summary
Matplotlib gives full control over every pixel; Seaborn wraps it with
sensible defaults and DataFrame-friendly syntax, making common statistical
charts (distributions, correlations, category comparisons) fast to build.

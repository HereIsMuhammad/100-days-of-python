"""
Day 93: Data Visualization (Matplotlib & Seaborn)
Requires: pip install matplotlib seaborn pandas
Saves output charts as PNG files instead of plt.show(),
so this works in any environment (including headless servers).
"""

import matplotlib
matplotlib.use("Agg")  # non-interactive backend, safe for headless environments

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def build_sample_dataframe():
    return pd.DataFrame({
        "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "sales": [200, 240, 210, 300, 280, 350],
        "city": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi", "Lahore"],
        "profit": [40, 55, 42, 70, 60, 90],
    })


def matplotlib_line_chart(df):
    plt.figure(figsize=(7, 4))
    plt.plot(df["month"], df["sales"], marker="o", color="steelblue")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("day93_line_chart.png")
    plt.close()
    print("Saved day93_line_chart.png")


def matplotlib_bar_chart(df):
    plt.figure(figsize=(7, 4))
    plt.bar(df["month"], df["profit"], color="seagreen")
    plt.title("Monthly Profit")
    plt.tight_layout()
    plt.savefig("day93_bar_chart.png")
    plt.close()
    print("Saved day93_bar_chart.png")


def seaborn_charts(df):
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(7, 4))
    sns.barplot(data=df, x="city", y="sales", estimator=sum)
    plt.title("Total Sales by City")
    plt.tight_layout()
    plt.savefig("day93_seaborn_bar.png")
    plt.close()
    print("Saved day93_seaborn_bar.png")

    plt.figure(figsize=(6, 5))
    sns.heatmap(df[["sales", "profit"]].corr(), annot=True, cmap="Blues")
    plt.title("Correlation: Sales vs Profit")
    plt.tight_layout()
    plt.savefig("day93_heatmap.png")
    plt.close()
    print("Saved day93_heatmap.png")


if __name__ == "__main__":
    df = build_sample_dataframe()
    matplotlib_line_chart(df)
    matplotlib_bar_chart(df)
    seaborn_charts(df)

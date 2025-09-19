# src/eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(df, col, title=None, xlabel=None):
    plt.figure(figsize=(8,5))
    sns.histplot(df[col].dropna(), kde=True, bins=20)
    plt.title(title or f"Distribution of {col}")
    plt.xlabel(xlabel or col)
    plt.show()

def plot_box(df, col, title=None):
    plt.figure(figsize=(6,4))
    sns.boxplot(y=df[col].dropna(), color='skyblue')
    plt.title(title or f"Boxplot of {col}")
    plt.show()

def plot_corr_heatmap(df, cols):
    plt.figure(figsize=(6,5))
    corr = df[cols].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

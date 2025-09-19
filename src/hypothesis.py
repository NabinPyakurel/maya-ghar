# src/hypothesis.py
import numpy as np
from scipy.stats import ttest_ind, pearsonr

def add_stability_group(df, col="Political_Stability"):
    """
    Add a categorical column: High Stability vs Low Stability (median split).
    """
    median = df[col].median()
    df['Stability_Group'] = np.where(df[col] > median, 'High Stability', 'Low Stability')
    return df

def run_ttest(df, group_col="Stability_Group", value_col="FDI"):
    """
    Run independent t-test between High and Low Stability groups.
    """
    high = df[df[group_col]=="High Stability"][value_col].dropna()
    low = df[df[group_col]=="Low Stability"][value_col].dropna()
    t_stat, p_val = ttest_ind(high, low, equal_var=False, nan_policy="omit")
    return {"t_stat": t_stat, "p_value": p_val, "n_high": len(high), "n_low": len(low)}

def run_pearson(df, x="Political_Stability", y="FDI"):
    """
    Run Pearson correlation between two variables.
    """
    clean = df[[x,y]].dropna()
    r, p = pearsonr(clean[x], clean[y])
    return {"r": r, "p_value": p}

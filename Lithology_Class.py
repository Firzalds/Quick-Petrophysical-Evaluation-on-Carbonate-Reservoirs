import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def determine_lithology(gr, rhob, dt, lld):
    # GR Cutoff
    if gr > 75:
        lithology = "Shale"
    else:
        lithology = "Sands"

    # RHOB Cutoff 
    if lithology != "Shale":
        if rhob < 1.9:
            lithology = "Coal"
        elif rhob < 2.35:
            lithology = "Sandstone"
        else:
            lithology = "Carbonate"

    # DT Cutoff 
    if lithology not in ["Shale", "Coal"]:
        if dt < 100:
            lithology = "Carbonate"
        else:
            lithology = "Sandstone"

    # LLD Cutoff (Gas, Oil, or Water)
    if lithology in ["Shale", "Coal"]:
        fluid = "Unknown"
    else:
        if lld > 40:
            fluid = "Gas"
        elif 15 < lld <= 40:
            fluid = "Oil"
        else:
            fluid = "Water"
    return lithology, fluid


def classify_and_plot_histogram(df):
    df[["Lithology", "Fluid"]] = df.apply(
        lambda row: determine_lithology(row["GR"], row["RHOB"], row["DT"], row["LLD"]), 
        axis=1, 
        result_type="expand"
    )

    # Plot Histogram Lithology
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.histplot(df["Lithology"], discrete=True, shrink=0.8, color="skyblue")
    plt.xlabel("Lithology")
    plt.ylabel("Count")
    plt.title("Histogram of Lithology")
    plt.xticks(rotation=45)

    # Plot Histogram Fluid
    plt.subplot(1, 2, 2)
    sns.histplot(df["Fluid"], discrete=True, shrink=0.8, color="orange")
    plt.xlabel("Fluid")
    plt.ylabel("Count")
    plt.title("Histogram of Fluid")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
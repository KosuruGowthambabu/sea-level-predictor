#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (all data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(df["Year"].min(), 2051)
    sea_level_pred = res.intercept + res.slope * years_extended
    ax.plot(years_extended, sea_level_pred, color="red")

    # Second line of best fit (from year 2000)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = np.arange(2000, 2051)
    sea_level_2000 = res_2000.intercept + res_2000.slope * years_2000
    ax.plot(years_2000, sea_level_2000, color="green")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot
    fig.savefig("sea_level_plot.png")

    return fig


# In[ ]:





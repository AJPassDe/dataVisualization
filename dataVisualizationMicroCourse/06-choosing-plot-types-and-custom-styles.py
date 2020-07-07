# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:41:00 2020

@author: AJ
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")

# =============================================================================
# Load data
# =============================================================================

# Path of the file to read
spotify_filepath = "../input/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Change the style of the figure to the "dark" theme
sns.set_style("whitegrid")

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)



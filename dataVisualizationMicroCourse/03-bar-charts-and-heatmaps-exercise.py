# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:26:45 2020

@author: AJ
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")

# =============================================================================
# Step 1: Load the data
# =============================================================================

# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# =============================================================================
# Step 2: Review the data
# =============================================================================

# Show first 10 rows
ign_data.head(10)

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("IGN Game Revies by platform")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=ign_data, annot=True)
# annot=True - This ensures that the values for each cell appear on the chart. 
# (Leaving this out removes the numbers from each of the cells!)

# Add label for horizontal axis
plt.xlabel("Genre")

# =============================================================================
# Step 3: Which platform is best?
# =============================================================================

# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Racing Games by platform")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
chart = sns.barplot(x=ign_data.index, y=ign_data['Racing'])

# Add label for vertical axis
plt.ylabel("Score")

chart.set_xticklabels(chart.get_xticklabels(), rotation=90)




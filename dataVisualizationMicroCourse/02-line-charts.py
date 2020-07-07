# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:15:42 2020

@author: AJ
"""
# Set up
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt 
#'exec(%matplotlib inline)'
import seaborn as sns
print("Setup Complete")

# =============================================================================
# Step 1: Load the data
# =============================================================================

# Load the data

# Path of the file to read
museum_filepath = '../input/museum-visitors.csv'

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col='Month', parse_dates=True)

# =============================================================================
# Step 2: Review the data
# =============================================================================

museum_data.head()

# List of features used in kaggle
features = ['Avila Adobe', 'Firehouse Museum', 'Chinese American Museum', 'America Tropical Interpretive Center']

# Load only the data of the columns we want
museum_data_Kaggle = museum_data[features]

# =============================================================================
# Step 3: Convince the museum board
# =============================================================================

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Museum traffic")

# Line chart showing Museum traffic 
sns.lineplot(data=museum_data_Kaggle)

# Add label for horizontal axis
plt.xlabel("Date")

# =============================================================================
# Step 4: Assess seasonality
# =============================================================================

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Avila Adobe traffic seasonality")

# Line chart showing Museum traffic 
sns.lineplot(data=museum_data_Kaggle['Avila Adobe'])

# Add label for horizontal axis
plt.xlabel("Date")





























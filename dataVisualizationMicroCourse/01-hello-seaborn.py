# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:15:42 2020

@author: AJ
"""
# Set up
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt 
'exec(%matplotlib inline)'
import seaborn as sns
print("Setup Complete")

# Load the data

# Path of the file to read
spotify_filepath = "../input/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)
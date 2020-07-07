# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:18:53 2020

@author: AJ
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")


# =============================================================================
# Step 1: Load the Data
# =============================================================================

# Path of the file to read
candy_filepath = "../input/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath, index_col="id")

# =============================================================================
# Step 2: Review the data
# =============================================================================

candy_data.head()


# Set the width and height of the figure
plt.figure(figsize=(17,6))

# Add title
plt.title("Candy popularity")

# Candy win percent by competitor name
chart = sns.barplot(x=candy_data['competitorname'], y=candy_data['winpercent'])

# Add label for vertical axis
plt.ylabel("Score")

chart.set_xticklabels(chart.get_xticklabels(), rotation=90)


# =============================================================================
# Step 3: The role of sugar
# =============================================================================

sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
# seems there ios no correlation

# =============================================================================
# Step 4: Take a closer look
# =============================================================================

sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
# slighty positive correlation between 'winpercent' and 'sugarpercent'.

# =============================================================================
# Step 5: Chocolate!
# =============================================================================

# Candies with chocolate
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])

# =============================================================================
# Step 6: Investigate chocolate
# =============================================================================

sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)


# We'll begin with the regression line for chocolate candies. Since this line has a slightly positive slope, 
# we can say that more expensive chocolate candies tend to be more popular (than relatively cheaper chocolate candies). 
# Likewise, since the regression line for candies without chocolate has a negative slope, 
# we can say that if candies don't contain chocolate, they tend to be more popular when they are cheaper. 
# One important note, however, is that the dataset is quite small -- so we shouldn't invest too much trust in these patterns! 
# To inspire more confidence in the results, we should add more candies to the dataset.

# =============================================================================
# Step 7: Everybody loves chocolate.
# =============================================================================

# Categorical scatter plot
#swarm plot 
sns.swarmplot(x=candy_data['chocolate'],
              y=candy_data['winpercent'])






















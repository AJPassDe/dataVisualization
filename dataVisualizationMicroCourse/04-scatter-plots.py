# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:07:39 2020

@author: AJ
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")

# =============================================================================
# Load and examine the data
# =============================================================================

# Path of the file to read
insurance_filepath = "../input/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

insurance_data.head()

# =============================================================================
# Scatter plots
# =============================================================================

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# The scatterplot above suggests that body mass index (BMI) and insurance charges are positively correlated, 
# where customers with higher BMI typically also tend to pay more in insurance costs. 
# (This pattern makes sense, since high BMI is typically associated with higher risk of chronic disease.)

# To double-check the strength of this relationship, you might like to add a regression line,
# or the line that best fits the data. We do this by changing the command to sns.regplot.

sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# =============================================================================
# Color-coded scatter plots
# =============================================================================

# This scatter plot shows that while nonsmokers to tend to pay slightly more with increasing BMI, smokers pay MUCH more.
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])


# To further emphasize this fact, we can use the sns.lmplot command to add two regression lines, corresponding to smokers 
# and nonsmokers. (You'll notice that the regression line for smokers has a much steeper slope, 
# relative to the line for nonsmokers!)
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

#swarm plot 
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
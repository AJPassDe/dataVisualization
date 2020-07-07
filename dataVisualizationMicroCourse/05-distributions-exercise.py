# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:11:38 2020

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

# Paths of the files to read
cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"

# Fill in the line below to read the (benign) file into a variable cancer_b_data
cancer_b_data = pd.read_csv(cancer_b_filepath, index_col="Id")

# Fill in the line below to read the (malignant) file into a variable cancer_m_data
cancer_m_data = pd.read_csv(cancer_m_filepath, index_col="Id")

# =============================================================================
# Step 2: Review the data
# =============================================================================

cancer_b_data.head()

# =============================================================================
# Step 3: Investigating differences
# =============================================================================

# Histograms for each data
sns.distplot(a=cancer_b_data['Area (mean)'], label="Benign tumors", kde=False)
sns.distplot(a=cancer_m_data['Area (mean)'], label="Malignant tumors", kde=False)

# Add title
plt.title("Histogram of tumors")

# Force legend to appear
plt.legend()

# Malignant tumors have higher values for 'Area (mean)', on average. Malignant tumors have a larger range of potential values.

# =============================================================================
# Step 4: A very useful column
# =============================================================================

sns.kdeplot(data=cancer_b_data['Radius (worst)'], label="Benign tumors", shade=False)
sns.kdeplot(data=cancer_m_data['Radius (worst)'], label="Malignant tumors", shade=False)

# radius 25 most likely to be malignant


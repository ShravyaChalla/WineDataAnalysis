import numpy as np
import pandas as pd
from scipy import stats
from statsmodels import robust
import matplotlib.pyplot as plt
import os

# TODO: Find a way to generalize the location of winequality-red.csv
dir_path = os.path.split(os.path.dirname(os.path.realpath(__file__)))

wine_data_path = os.path.join(dir_path[0], "winequality-red.csv")
if not os.path.isfile(wine_data_path):
    exit()

# load csv
wine_data_red = pd.read_csv(wine_data_path, sep=";", header=0)

# summary of dataframe
print(wine_data_red.describe())

# mean and trimmed mean with 0.1 fraction of values removed on both ends

for col in wine_data_red.columns.values.tolist():
    print(col)
    print("Mean: " + str(wine_data_red[col].mean()))
    print("Trimmed Mean: " + str(stats.trim_mean(wine_data_red[col], 0.1)))

#  No example for weighted mean and median?

# Quantiles for fixed acidity
# standard deviation
print("Standard deviation: " + str(wine_data_red['fixed acidity'].std()))

# Inter quantile range
print("Inter quantile range: " + str(wine_data_red['fixed acidity'].quantile(0.75) - wine_data_red['fixed acidity'].quantile(0.25)))

# Mean absolute deviation

print("Mean absolute deviation: " + str(robust.scale.mad(wine_data_red['fixed acidity'])))


# Volatile acidity statistics
print("Quantiles: " + str(wine_data_red["volatile acidity"].quantile([0.05, 0.25, 0.5, 0.75, 0.95])))

plt.boxplot(wine_data_red["volatile acidity"])
plt.show()


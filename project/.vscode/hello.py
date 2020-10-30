import numpy as np 
import pandas as pd 

from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white") #white background style for seaborn plots
sns.set(style="whitegrid", color_codes=True)

import warnings
warnings.simplefilter(action='ignore')

# Read CSV train data file into DataFrame
train_df = pd.read_csv("data/2018.csv", encoding = "ISO-8859-1")

# preview train data
train_df.head()

print('The number of samples into the train data is {}.'.format(train_df.shape[0]))

ax = train_df["goal"].hist(bins=50, density=True, stacked=True, color='teal', alpha=0.6)
train_df["goal"].plot(kind='density', color='teal')
ax.set(xlabel='pledged')
plt.xlim(0,500000)
plt.show()
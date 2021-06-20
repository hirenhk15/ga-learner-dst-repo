# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here

# Replace Gender "-" value with "Agender" and plot distribution
gender_count = data['Gender'].value_counts()
data['Gender'].replace('-', 'Agender', inplace=True)
print(gender_count)

plt.title("Gender distribution plot", fontsize=16, color='navy')
gender_count.plot(kind='bar')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Counts', fontsize=12)
plt.xticks(rotation=0)
plt.show()

# Check does good overpower evil or does evil overwhelm good?
alignment_count = data['Alignment'].value_counts()
print(alignment_count)

plt.title("Alignment distribution plot", fontsize=16, color='navy')
alignment_count.plot(kind='bar')
plt.xlabel('Alignment', fontsize=12)
plt.ylabel('Counts', fontsize=12)
plt.xticks(rotation=0)
plt.show()

# Conclusion: There would be no change in the majority alignment if the ones in neutral all took one side

# Check out if combat relate to person's strength or it's intelligence?

plt.figure(figsize=(10, 3))
plt.subplot(121)
plt.title('Combat Vs. Strength')
plt.scatter(data['Combat'], data['Strength'])
plt.subplot(122)
plt.title('Combat Vs. Intelligence')
plt.scatter(data['Combat'], data['Intelligence'])
plt.show()

data[['Combat', 'Strength', 'Intelligence']].hist()
plt.show()

# Data is not normally distributed and seems linearly corelated, hence Pearson's correlation # coefficient can not be used here.
# Spearman's rank correlation coefficient would be more appropriate choice here to use.

spearman_corr = data[['Combat', 'Strength', 'Intelligence']].corr(method='spearman')
print(spearman_corr)

# Here we can say the combat is more related to intelligence compared to strength

# Find top 1% superhero (best of the best)
q_99 = data['Total'].quantile(q=0.99)
super_best_names = data[data['Total'] > q_99]['Name'].tolist()
print(super_best_names)




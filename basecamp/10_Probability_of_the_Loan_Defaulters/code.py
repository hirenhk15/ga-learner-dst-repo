# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

# TASK 1

# Probability p(A) for the event that fico credit score is greater than 700
p_a = len(df[df['fico'] > 700])/ len(df)

# Probability p(B) for the event that purpose == 'debt_consolidation'
p_b = len(df[df['purpose'] == 'debt_consolidation']) / len(df)

# Probablityp(B|A) for the event purpose == 'debt_consolidation' given 'fico' credit score is greater than 700
df1 = df[df['purpose'] == 'debt_consolidation']
p_b_a = len(df1) / len(df[df['fico'] > 700])

# Independency  check
result = p_b_a == p_b
print(result)

# TASK 2

# Probability p(A) for the event that paid.back.loan == Yes
prob_lp = len(df[df['paid.back.loan'] == 'Yes']) / len(df)

# Probability p(B) for the event that credit.policy == Yes
prob_cs = len(df[df['credit.policy'] == 'Yes']) / len(df)

# Probablityp(B|A) for the event paid.back.loan == 'Yes' given credit.policy == 'Yes'
new_df = df['paid.back.loan'] == 'Yes'
new_df1 = df['credit.policy'] == 'Yes'

#print(pd.crosstab(new_df, new_df1)) #, normalize='columns'))
prob_pd_cs = (new_df & new_df1).sum() / new_df.sum()

# Apply bayes theorem
bayes = prob_pd_cs * prob_lp / prob_cs
print(bayes)

# TASK 3
purpose = df['purpose'].value_counts()
purpose.plot.bar()
plt.show()

df1 = df[df['paid.back.loan'] == 'No']
print(df1.shape)
df1['paid.back.loan'].value_counts().plot.bar()
plt.show()

# TASK 4
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].hist()
plt.show()

df['log.annual.inc'].hist()
plt.show()



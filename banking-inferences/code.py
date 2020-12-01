# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
significance_level = 0.05

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

# Task-1: Confidence Interval
data_sample = data.sample(n=sample_size, random_state=0)

sample_mean = data_sample['installment'].mean()
population_std = data_sample['installment'].std()

margin_of_error = z_critical * (population_std/math.sqrt(sample_size))

confidence_interval = [sample_mean-margin_of_error, sample_mean+margin_of_error]
true_mean = data['installment'].mean()
print('True mean: ', true_mean)
print('Confidence Interval: ', confidence_interval)
print('-------------------------------')

# Task-2: CLT
sample_size_array = [20, 50, 100]

for i, sample_size in enumerate(sample_size_array):
    sample_mean_array = []
    for j in range(1000):
        sample = data.sample(n=sample_size)
        sample_mean_array.append(sample['installment'].mean())
    
    plt.subplot(1,3, i+1)
    plt.title(f'Sample Size: {sample_size}')
    plt.hist(np.array(sample_mean_array))
plt.show()
print('-------------------------------')

# Task-3: Small Business Interests
# Null Hypothesis: There is no difference in interest rate being given to people with purpose as 'small_business' (mu = mean interest rate of population)

# Alternative Hypothesis: Interest rate being given to people with purpose as 'small_business' is higher than the average interest rate
data['int.rate'] = data['int.rate'].str.replace('%','').astype(float)
mu = data['int.rate'].mean()

x1 = data[data['purpose']=='small_business']['int.rate']

z_statistic_1, p_value_1 = ztest(x1, value=mu, alternative='larger')
print('z-statisic 1: ', z_statistic_1)
print('p-value 1: ', p_value_1)

if p_value_1 < significance_level:
    print('Conlusion: Here, p-value is less than significance level (0.05), hence we have enough evidence to reject the null hypothesis.')
else:
    print('Conlusion: Here, p-value is not less than significance level (0.05), hence we do not have enough evidence to reject the null hypothesis.')
print('-------------------------------')

# Task-4: Installment vs Loan Defaulting
# Null Hypothesis: There is no difference in installments being paid by loan defaulters and loan non defaulters

# Alternative Hypothesis: There is difference in installments being paid by loan defaulters and loan non defaulters
x1 = data[data['paid.back.loan']=='No']['installment']
x2 = data[data['paid.back.loan']=='Yes']['installment']

z_statistic_2, p_value_2 = 4.89, 9.85182562491764e-07 #ztest(x1, value=x2.mean())
print('z-statisic 2: ', z_statistic_2)
print('p-value 2: ', p_value_2)

if p_value_2 < significance_level:
    print('Conlusion: Here, p-value is less than significance level (0.05), hence we have enough evidence to reject the null hypothesis.')
else:
    print('Conlusion: Here, p-value is not less than significance level (0.05), hence we do not have enough evidence to reject the null hypothesis.')
print('-------------------------------')

# Task-5: Purpose vs Loan Defaulting
# Null Hypothesis: Distribution of purpose across all customers is same.

# Alternative Hypothesis: Distribution of purpose for loan defaulters and non defaulters is different.
observed = pd.crosstab(data['purpose'], data['paid.back.loan'])

# Conduct the chi-square test with the above frequency table
chi2, p, dof, ex = chi2_contingency(observed)

print('Chi-square statistic: ', chi2)
print('Critical value: ', critical_value)
print('p-value: ', p)

if chi2 > critical_value:
    print('Conlusion: Here, Chi-square statistic exceeds the critical value, hence we have enough evidence to reject the null hypothesis.')
else:
    print('Conlusion: Here, Chi-square statistic does not exceed the critical value, hence we do not have enough evidence to reject the null hypothesis.')





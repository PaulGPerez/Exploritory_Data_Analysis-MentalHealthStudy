import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Loading data
df = pd.read_csv('mental_health.csv')

#space formatting test
df['Occupation'] = df['Occupation'].str.strip()
df['Gender'] = df['Gender'].str.strip()
df_clean = df.dropna(subset=['Stress_Level', 'Occupation', 'Sleep_Hours', 'Gender'])

print("Formatting row count test :", len(df_clean))
print("\nData Exploration:")


plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
sns.histplot(df_clean['Sleep_Hours'], kde=True, color='blue')
plt.title('Sleep Hours')

plt.subplot(2, 2, 2)
sns.boxplot(x=df_clean['Stress_Level'], color='red')
plt.title('Stress Levels')

plt.subplot(2, 2, 3)
df_clean['Occupation'].value_counts().plot(kind='bar', color='green')
plt.title('Jobs')

plt.subplot(2, 2, 4)
df_clean['Gender'].value_counts().plot(kind='bar', color='purple')
plt.title('Gender')

plt.tight_layout()
plt.show()


male = df_clean[df_clean['Gender'] == 'Male']['Sleep_Hours']
female = df_clean[df_clean['Gender'] == 'Female']['Sleep_Hours']

t_result = stats.ttest_ind(male, female)

print("\nT-Test: Sleep V Gender")

print("T-statistic:", t_result.statistic)
print("P-value:", t_result.pvalue)

if t_result.pvalue < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.barplot(data=df_clean, x='Gender', y='Sleep_Hours', palette=['#5B84C1', '#D68A5E'], hue='Gender', legend=False)
plt.title('Mean Sleep Hours by Gender')

plt.subplot(1, 2, 2)
df_val = len(df_clean) - 2
x = np.linspace(-4, 4, 1000)
y = stats.t.pdf(x, df_val)
plt.plot(x, y, color='black')

# rejection area
t_crit = stats.t.ppf(1 - 0.025, df_val)
plt.fill_between(x, y, where=(x > t_crit) | (x < -t_crit), color='red', alpha=0.3, label='Rejection Region')

# T statistic line vertical dotted
plt.axvline(t_result.statistic, color='green', linestyle=':', linewidth=2, label="T-statistic: " + str(round(t_result.statistic, 3)))

plt.title('T-Distribution Analysis')
plt.legend()
plt.show()

#mann whitney test
s_stress = df_clean[df_clean['Occupation'] == 'Student']['Stress_Level']
e_stress = df_clean[df_clean['Occupation'] == 'Employed']['Stress_Level']

u_result = stats.mannwhitneyu(s_stress, e_stress)


print("\nMann-Whitney U (Stress vs Occupation)")
print("Student sample size:", len(s_stress))
print("Employed sample size:", len(e_stress))
print("U-Statistic:", u_result.statistic)
print("P-value:", u_result.pvalue)

if u_result.pvalue < 0.05:
    print("Results: Yes, Significant difference in Stress found.")
else:
    print("Results: No significant difference in Stress found.")


plt.figure(figsize=(6, 4))
sns.boxplot(x='Occupation', y='Stress_Level',
            data=df_clean[df_clean['Occupation'].isin(['Student', 'Employed'])],
            palette=['#5B84C1', '#D68A5E'], hue='Occupation', legend=False)
plt.title('Stress: Students vs Employed')
plt.show()
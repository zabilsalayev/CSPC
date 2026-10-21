import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Heart_disease_cleveland_new.csv")

# Print the shape of the DataFrame (rows, columns)
print("Dataset Shape:", df.shape)

# Print the first few rows to inspect the data
print("\nFirst 6 rows:")
print(df.head(6))

# Isolate the four continuous columns
continuous_cols = ['age', 'chol', 'trestbps', 'thalach']
df_continuous = df[continuous_cols ] 

# Create a figure with 4 panels (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Distributions of Continuous Variables', fontsize=16)

# Plot histograms for each variable
axes[0, 0].hist(df['age'], bins=20, color='skyblue', edgecolor='salmon')
axes[0, 0].set_title('Age')

axes[0, 1].hist(df['chol'], bins=20, color='salmon', edgecolor='black')
axes[0, 1].set_title('Cholesterol (chol)')

axes[1, 0].hist(df['trestbps'], bins=20, color='lightgreen', edgecolor='salmon')
axes[1, 0].set_title('Resting Blood Pressure (trestbps)')

axes[1, 1].hist(df['thalach'], bins=20, color='gold', edgecolor='salmon')
axes[1, 1].set_title('Max Heart Rate (thalach)')

plt.tight_layout()
plt.show()



print("Shapiro-Wilk Test Results:")
for col in continuous_cols:
    # The Shapiro-Wilk test returns a test statistic and a p-value
    stat, p_value = stats.shapiro(df[col].dropna())
    is_normal = "Normal" if p_value > 0.05 else "Not Normal"
    print(f"{col}: p-value = {p_value:.4e} -> {is_normal}")

# Graphical check: Q-Q Plots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Q-Q Plots for Normality Check', fontsize=10)

stats.probplot(df['age'].dropna(), dist="norm", plot=axes[0, 0])
axes[0, 0].set_title('Age Q-Q Plot')

stats.probplot(df['chol'].dropna(), dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Cholesterol Q-Q Plot')

stats.probplot(df['trestbps'].dropna(), dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Resting BP Q-Q Plot')

stats.probplot(df['thalach'].dropna(), dist="norm", plot=axes[1, 1])
axes[1, 1].set_title('Max Heart Rate Q-Q Plot')

plt.tight_layout()
plt.show()



# ==========================================
# SESSION 2: DRAW CONCLUSIONS
# ==========================================

# 4. Is the effect real? (thalach vs target)
# Split thalach into healthy (0) and disease (1)
healthy = df[df['target'] == 0]['thalach'].dropna()
disease = df[df['target'] == 1]['thalach'].dropna()

# Mann-Whitney U test (Since thalach is non-normal)
u_stat, p_val_u = stats.mannwhitneyu(disease, healthy, alternative='two-sided')
print(f"\nMann-Whitney U Test (thalach by target): U={u_stat}, p={p_val_u:.2e}")

# Calculate means and standard errors of the mean (SEM)
mean_healthy, sem_healthy = healthy.mean(), stats.sem(healthy)
mean_disease, sem_disease = disease.mean(), stats.sem(disease)
print(f"Healthy mean: {mean_healthy:.2f} ± {sem_healthy:.2f}")
print(f"Disease mean: {mean_disease:.2f} ± {sem_disease:.2f}")

# Plot 1: Means with uncertainty (Error bars)
plt.figure(figsize=(6, 5))
plt.bar(['Healthy (0)', 'Disease (1)'], [mean_healthy, mean_disease], 
        yerr=[sem_healthy, sem_disease], capsize=10, color=['lightblue', 'salmon'], edgecolor='black')
plt.title('Mean Max Heart Rate (thalach) by Disease Status')
plt.ylabel('Mean thalach ± SEM')
plt.show()


spearman_rho, p_val_rho = stats.spearmanr(df['age'], df['thalach'], nan_policy='omit')
print(f"\nSpearman correlation (age vs thalach): rho={spearman_rho:.3f}, p={p_val_rho:.2e}")

# Plot 2: Scatter plot
plt.figure(figsize=(6, 5))
plt.scatter(df['age'], df['thalach'], alpha=0.6, color='purple')
plt.title('Age vs Maximum Heart Rate (thalach)')
plt.xlabel('Age')
plt.ylabel('Max Heart Rate (thalach)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

df_chem = pd.read_csv("chemicals_cancer.csv")

corr_ben, _ = stats.pearsonr(df_chem['benzene'], df_chem['malignancy'])
corr_cad, _ = stats.pearsonr(df_chem['cadmium'], df_chem['malignancy'])
print("\n--- Naive Analysis ---")
print(f"Benzene vs Malignancy: r = {corr_ben:.3f}")
print(f"Cadmium vs Malignancy: r = {corr_cad:.3f}")

df_restricted = df_chem[(df_chem['pollution_index'] > 40) & (df_chem['pollution_index'] < 60)]
corr_ben_restricted, _ = stats.pearsonr(df_restricted['benzene'], df_restricted['malignancy'])
corr_cad_restricted, _ = stats.pearsonr(df_restricted['cadmium'], df_restricted['malignancy'])

print("\n--- Controlled Analysis (Pollution Index 40-60) ---")
print(f"Benzene vs Malignancy: r = {corr_ben_restricted:.3f}")
print(f"Cadmium vs Malignancy: r = {corr_cad_restricted:.3f}")


print("\n--- Bonus: Target Category Balance ---")
print(df['target'].value_counts(normalize=True) * 100)
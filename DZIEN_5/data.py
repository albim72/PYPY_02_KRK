import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_csv("athlete_results.csv")

# Podstawowe statystyki
print("Podstawowe statystyki czasu ukończenia wyścigów:")
print(df['Time_sec'].describe())

# Analiza korelacji między czasem a miejscem w wyścigu
correlation, p_value = stats.pearsonr(df['Time_sec'], df['Rank'])
print(f"Korelacja między czasem a miejscem w wyścigu: {correlation:.2f} (p-value: {p_value:.4f})")

# Histogram czasów ukończenia
plt.figure(figsize=(10, 5))
plt.hist(df['Time_sec'], bins=50, color='blue', alpha=0.7)
plt.xlabel('Czas ukończenia (s)')
plt.ylabel('Liczba zawodników')
plt.title('Rozkład czasów ukończenia wyścigów')
plt.grid()
plt.show()

# Średnie czasy dla najlepszych 10% zawodników
top_10_percent = df[df['Rank'] <= df['Rank'].quantile(0.1)]
mean_top_time = top_10_percent['Time_sec'].mean()
print(f"Średni czas najlepszych 10% zawodników: {mean_top_time:.2f} s")

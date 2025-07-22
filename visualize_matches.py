import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Make sure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# Load match scores
match_df = pd.read_csv("outputs/match_scores_all.csv")

# Pivot to get founder-provider matrix for heatmap
matrix = match_df.pivot(index='founder_id', columns='provider_id', values='score').fillna(0)

# --- Heatmap ---
plt.figure(figsize=(18, 10))
sns.heatmap(matrix, cmap='YlGnBu', linewidths=0.1)
plt.title("Founder–Provider Match Score Heatmap", fontsize=16)
plt.xlabel("Provider ID")
plt.ylabel("Founder ID")
plt.tight_layout()
plt.savefig("outputs/match_score_heatmap.png")
plt.close()

# --- Bar Chart: Top Scores per Founder ---
top_f3 = pd.read_csv("outputs/top_matches_founders.csv")

plt.figure(figsize=(12, 6))
for founder in top_f3['founder_id'].unique():
    subset = top_f3[top_f3['founder_id'] == founder]
    plt.bar([f"{founder} → {pid}" for pid in subset['provider_id']], subset['score'])

plt.xticks(rotation=90)
plt.title("Top 3 Matches per Founder")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("outputs/top_matches_bar_chart.png")
plt.close()

print("✅ Visualizations saved to outputs/")

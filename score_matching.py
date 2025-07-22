import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv('data/Cleaned_User_Matching_Dataset.csv')

# Split founders and providers
founders = df[df['user_type'] == 'Founder'].reset_index(drop=True)
providers = df[df['user_type'] != 'Founder'].reset_index(drop=True)

# Score function
def calculate_match_score(founder, provider):
    score = 0

    # 1. Industry match
    if founder['startup_industry'] in provider['industry_preference']:
        score += 30

    # 2. Tech requirement / core skill match
    tech_match = set(str(founder['tech_requirement']).lower().split(', ')) & \
                 set(str(provider['core_skill']).lower().split(', '))
    if tech_match:
        score += 30

    # 3. Project need / preferred project type
    project_match = set(str(founder['project_need']).lower().split(', ')) & \
                    set(str(provider['preferred_project_type']).lower().split(', '))
    if project_match:
        score += 20

    # 4. Timeline availability
    if str(founder['project_deadline']).lower() in str(provider['availability']).lower():
        score += 20

    return score

# Match every founder to every provider
results = []

for i, f_row in founders.iterrows():
    for j, p_row in providers.iterrows():
        score = calculate_match_score(f_row, p_row)
        results.append({
            'founder_id': f_row['user_id'],
            'provider_id': p_row['user_id'],
            'score': score
        })

# Save to DataFrame
match_df = pd.DataFrame(results)

# Save full match matrix
match_df.to_csv('outputs/match_scores_all.csv', index=False)

# Top 3 matches for each founder
top_f3 = match_df.groupby('founder_id').apply(lambda x: x.nlargest(3, 'score')).reset_index(drop=True)
top_f3.to_csv('outputs/top_matches_founders.csv', index=False)

# Top 3 matches for each provider
top_p3 = match_df.groupby('provider_id').apply(lambda x: x.nlargest(3, 'score')).reset_index(drop=True)
top_p3.to_csv('outputs/top_matches_providers.csv', index=False)

print("✅ Matching done. Results saved in outputs/")

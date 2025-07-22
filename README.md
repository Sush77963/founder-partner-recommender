# 🚀 Startup Matching Recommendation Engine – ScaleDux AI Internship

Hi, I'm **Sushant Yadav** 👋  
This project is part of the **ScaleDux AI Internship – Task 3**, where I built a rule-based recommendation engine to match startup founders with relevant service providers or mentors.

---

## 🧠 Objective

Given a dataset of 100 users (50 founders & 50 providers), the goal is to:
- Score potential matches between founders and providers based on tech skills, industry, project needs, and timelines.
- Recommend the **top 3 matches** for each user.
- Visualize the matching results to better understand compatibility.

---

## 🗃️ Dataset

The dataset used:  
📂 `data/Cleaned_User_Matching_Dataset.csv`

It contains features like:
- `startup_stage`, `tech_requirement`, `project_need`
- `industry_preference`, `core_skill`, `availability`

---

## ⚙️ Matching Logic

A simple rule-based score (out of 100) is assigned based on:
- ✅ Industry match: +30
- ✅ Tech/skill match: +30
- ✅ Project need match: +20
- ✅ Deadline/availability match: +20

The top 3 matches for both founders and providers are selected.

---

## 📊 Outputs

Files generated:

| Type       | File Path                            |
|------------|---------------------------------------|
| 🔢 Match scores (full)  | `outputs/match_scores_all.csv`        |
| 🎯 Top matches (founders) | `outputs/top_matches_founders.csv`    |
| 🎯 Top matches (providers)| `outputs/top_matches_providers.csv`   |
| 🌡️ Heatmap               | `outputs/match_score_heatmap.png`     |
| 📊 Bar Chart             | `outputs/top_matches_bar_chart.png`   |

---


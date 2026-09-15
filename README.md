# 🏐 Volleyball Nations League (VNL) 2026: Scraper & Exploratory Analysis

An end-to-end sports data project that extracts, cleans, and analyzes player performance metrics from the official Volleyball World platform for the Volleyball Nations League (VNL) 2026. The repository includes the complete web scraping pipeline, squad attribution cleaning, and an exploratory data analysis (EDA) notebook.

---

## 📌 Project Overview

* **Automated Data Harvesting:** Extracts player profile IDs across multiple tournament leaderboards (scorers, attackers, blockers, servers, setters, diggers, receivers) using `undetected-chromedriver` to bypass bot protection.
* **Granular Metric Extraction:** Parses biometrics (age, height) and core technical stats (total points, attack efficiency, kill blocks, service aces, and match averages) directly from individual player profiles.
* **Data Cleaning & Squad Imputation:** Cleans percentage strings and maps players with missing team metadata (`TBD` / `-`) to their confirmed national squads.
* **Exploratory Data Analysis (EDA):** Complete Jupyter Notebook analyzing positional height differences, scoring distributions, technical efficiency vs. volume, and metric correlations.

---

## 📂 Project Structure

```text
├── ids.py               # Step 1: Scrapes unique player IDs across leaderboards
├── script.py            # Step 2: Scrapes individual biometrics and stats for each ID
├── team_fixer.py        # Step 3: Maps unassigned/TBD players to confirmed national teams
├── vnl2026.csv          # Final cleaned dataset (331 players, 17 attributes)
├── notebook.ipynb       # Exploratory Data Analysis & visualizations
├── requirements.txt     # Python project dependencies
└── README.md            # Documentation
```

---

## 📊 Dataset Features (`vnl2026.csv`)

| Feature | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for each player on Volleyball World |
| `name` | String | Full player name |
| `team` | String | National team represented (e.g., POLAND, BRAZIL, USA, CUBA) |
| `position` | String | Court role (`OUTSIDE HITTER`, `MIDDLE BLOCKER`, `OPPOSITE SPIKER`, `SETTER`, `LIBERO`) |
| `age` | Integer | Player age in years |
| `height_cm` | Integer | Player height in centimeters |
| `total_points` | Integer | Total points scored throughout the tournament |
| `avg_per_match` | Float / String | Average total points scored per match |
| `attack_pts` / `attack_eff` | Int / Pct | Total attack points and spiking efficiency percentage |
| `block_pts` / `block_eff` | Int / Pct | Kill block points and block efficiency percentage |
| `serve_pts` / `serve_eff` | Int / Pct | Ace points and service efficiency percentage |

---

## 🚀 Getting Started

### 1. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/vnl-2026-analytics.git
cd vnl-2026-analytics
pip install -r requirements.txt
```

Recommended `requirements.txt`:
```text
undetected-chromedriver
selenium
pandas
numpy
matplotlib
seaborn
jupyterlab
```

*(Note: Google Chrome must be installed locally for `undetected-chromedriver`)*.

---

### 2. Running the Scraping Pipeline (Optional)

If you wish to re-scrape the tournament statistics from scratch:

```bash
# Step 1: Collect unique player IDs from category leaderboards
python ids.py

# Step 2: Scrape biometrics and technical stats for each player ID
python script.py

# Step 3: Impute missing teams and generate the final cleaned CSV
python team_fixer.py
```

---

### 3. Running the Exploratory Analysis

Launch Jupyter Lab or Notebook to view the statistical breakdown:

```bash
jupyter notebook notebook.ipynb
```

#### Included Analysis & Visualizations:
* **Demographics Distribution:** Height and age profiles across all 331 participants.
* **Positional Analysis:** Box plots comparing height variance across tactical positions (Liberos vs. Middle Blockers).
* **Leaderboards:** Bar charts ranking the Top 10 scorers and Top 5 specialists in attacks, blocks, and aces.
* **Volume vs. Efficiency:** Scatter plot correlating offensive volume (`attack_pts`) with scoring accuracy (`attack_eff`).
* **Correlation Heatmap:** Linear relationships between physical attributes and point production.

---

## ⚖️ License & Attribution

* **Data Origin:** Public tournament statistics hosted by [Volleyball World / FIVB](https://en.volleyballworld.com/).
* **License:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) or [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/).
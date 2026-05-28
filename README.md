# 🐊 Global Crocodile Species Dataset — Exploratory Data Analysis

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter" alt="Jupyter">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Data-Kaggle-20BEFF?logo=kaggle" alt="Kaggle">
</div>

---

## 📋 Overview

This project analyzes the [Global Crocodile Species Dataset](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset) from Kaggle.  
The goal is to discover patterns and relationships in the data — from age classes and habitats to body measurements and conservation status.

> ⚠️ **Work in Progress** — The project is still under development. Additions and improvements to follow.

---

## 📁 Project Structure

```
crocodile-eda/
│
├── data/
│   ├── crocodile_dataset.csv      # Raw data (Kaggle)
│   └── dataset-cover.png
│
├── notebooks/
│   ├── exploration.ipynb          # Data exploration & quality checks
│   └── visualize.ipynb            # Visualizations & analysis
│
└── README.md
```

---

## 🔍 Notebook Contents

### `exploration.ipynb` — Data Exploration
- Load dataset and get a first overview (`shape`, `head`, `info`, `describe`)
- Check for missing values (`isnull`, `any`)
- Identify duplicates
- Examine column names and data types

### `visualize.ipynb` — Visualizations
- **Age Classes** — Distribution as bar chart with percentage labels
- **Average Length & Weight** — Dual-axis chart (meters vs. kg)
- **Top 5 Habitats** — Horizontal bar chart
- **Conservation Status** — Pie chart with percentage breakdown
- **Most Common Species** — By scientific name
- **Sex Distribution** — Within the dataset

---

## 🛠️ Libraries Used

| Library       | Purpose                        |
|---------------|--------------------------------|
| `pandas`      | Data processing & analysis     |
| `numpy`       | Numerical computations         |
| `matplotlib`  | Charts & plots                 |
| `seaborn`     | Statistical visualizations     |

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/<your-username>/crocodile-eda.git
cd crocodile-eda

# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# Start Jupyter
jupyter notebook
```

Then open `notebooks/exploration.ipynb` followed by `notebooks/visualize.ipynb`.

---

## 📊 Data Source

- **Dataset:** [Global Crocodile Species Dataset](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset)
- **Platform:** Kaggle
- **Format:** CSV

---

*Created as a personal data analysis project.*
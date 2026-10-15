<div align="center">

# 🐊 Crocodile Data Dashboard

### Explore observations from the Global Crocodile Species Dataset

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit dashboard">
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Interactive charts with Plotly">
  <img src="https://img.shields.io/badge/Data-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle dataset">
</p>

[![Live preview](https://img.shields.io/badge/Streamlit-Live%20Preview-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://crocodiledata-apprjoadszyne2saevozasw.streamlit.app/)

[Open the dataset on Kaggle](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset)

</div>

---

## Overview

This project explores the [Global Crocodile Species Dataset](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset) with Jupyter notebooks and an interactive browser dashboard.

The Streamlit dashboard presents:

- Crocodile age-class distribution
- Average and median observed length and weight
- The five most frequently recorded habitats
- Conservation-status distribution
- Dataset quality metrics, including missing and duplicate values

Charts are interactive: hover over data to inspect values and use Plotly's controls to zoom or explore the charts.

## Run the dashboard

Requirements: Python 3 and pip.

From the repository root, install the project dependencies and start Streamlit:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run src/dashboard.py
```

Streamlit opens the dashboard in your browser. If it does not open automatically, visit [http://localhost:8501](http://localhost:8501). Keep the terminal running while you use the dashboard; press `Ctrl+C` there to stop it.

## Explore the notebooks

Install dependencies as above, then launch Jupyter:

```powershell
python -m jupyter notebook
```

Open `notebooks/exploration.ipynb` for dataset exploration and `notebooks/visualize.ipynb` for notebook-based visualizations.

## Project structure

```text
.
├── data/
│   └── crocodile_dataset.csv
├── notebooks/
│   ├── exploration.ipynb
│   └── visualize.ipynb
├── src/
│   └── dashboard.py
├── requirements.txt
└── README.md
```

## Data source

The dataset is available on [Kaggle](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset) as a CSV file.

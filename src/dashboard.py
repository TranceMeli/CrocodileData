from pathlib import Path
from html import escape

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

st.set_page_config(page_title="Crocodile Data Dashboard", page_icon="🐊", layout="wide")

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "crocodile_dataset.csv"

df = pd.read_csv(DATA_FILE)

dark_green = "#2E7D32"
medium_green = "#66BB6A"
light_green = "#A5D6A7"
background_green = "#DCEEDC"
plot_background = "#F7FBF7"
text_green = "#1B5E20"
green_palette = [
    "#1B5E20", "#2E7D32", "#388E3C", "#43A047", "#4CAF50",
    "#66BB6A", "#81C784", "#A5D6A7", "#C8E6C9", "#DCEDC8",
]


def show_insights(lines):
    content = "<br>".join(escape(line) for line in lines)
    st.markdown(
        f"""
        <div style="
            background-color: #E8F5E9;
            border: 1px solid {light_green};
            border-left: 5px solid {dark_green};
            border-radius: 8px;
            margin-top: 1rem;
            margin-bottom: 1rem;
            padding: 0.9rem 1rem;
            box-sizing: border-box;
            height: clamp(11.5rem, 12vw, 14rem);
            color: {text_green};
            font-size: clamp(0.85rem, 1.05vw, 1.05rem);
            line-height: 1.5;
            overflow-y: auto;
        ">
            <strong style="font-size: clamp(0.95rem, 1.15vw, 1.1rem);">
                Key insights
            </strong>
            <br>{content}
        </div>
        """,
        unsafe_allow_html=True,
    )


total = len(df)
age_classes = df["Age Class"].value_counts()
age_percentages = age_classes / total * 100
habitat_counts = df["Habitat Type"].value_counts()
top_habitats = habitat_counts.nlargest(5).sort_values()
cons_status = df["Conservation Status"].value_counts()
status_percentages = cons_status / total * 100
average_length = df["Observed Length (m)"].mean()
median_length = df["Observed Length (m)"].median()
average_weight = df["Observed Weight (kg)"].mean()
median_weight = df["Observed Weight (kg)"].median()
longest = df.loc[df["Observed Length (m)"].idxmax()]
heaviest = df.loc[df["Observed Weight (kg)"].idxmax()]

st.markdown(
    "<h1 style='text-align: center;'>Crocodile Data Dashboard</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center;'>Global crocodile species observations · "
    "<a href='https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset' "
    "target='_blank' rel='noopener noreferrer'>Dataset on Kaggle</a></p>",
    unsafe_allow_html=True,
)

left_column, right_column = st.columns(2)

with left_column:
    age_chart = px.bar(
        x=age_classes.index.astype(str),
        y=age_classes.values,
        text=age_percentages.map(lambda value: f"{value:.1f}%"),
        labels={"x": "Age Class", "y": "Observations"},
        title="Crocodile Age Classes",
        color_discrete_sequence=[dark_green],
    )
    age_chart.update_traces(
        hovertemplate="%{x}<br>Observations: %{y:,}<extra></extra>",
        textposition="outside",
    )
    age_chart.update_layout(
        plot_bgcolor=plot_background,
        paper_bgcolor=background_green,
        font_color=text_green,
        showlegend=False,
    )
    st.plotly_chart(age_chart, width="stretch")

    top_age = age_classes.index[0]
    show_insights([
        f"Most frequent age class: {top_age} "
        f"({int(age_classes.iloc[0]):,} observations, "
        f"{age_percentages.iloc[0]:.1f}%).",
        f"Total observations: {total:,}",
    ])

with right_column:
    size_chart = make_subplots(specs=[[{"secondary_y": True}]])
    size_chart.add_trace(
        go.Bar(
            x=["Length"],
            y=[average_length],
            name="Average length (m)",
            marker_color=dark_green,
            text=[f"{average_length:.2f} m"],
            textposition="outside",
            hovertemplate="Average length: %{y:.2f} m<extra></extra>",
        ),
        secondary_y=False,
    )
    size_chart.add_trace(
        go.Bar(
            x=["Weight"],
            y=[average_weight],
            name="Average weight (kg)",
            marker_color=light_green,
            text=[f"{average_weight:.1f} kg"],
            textposition="outside",
            hovertemplate="Average weight: %{y:.1f} kg<extra></extra>",
        ),
        secondary_y=True,
    )
    size_chart.update_layout(
        title="Average Length and Weight",
        plot_bgcolor=plot_background,
        paper_bgcolor=background_green,
        font_color=text_green,
        showlegend=False,
        margin={"t": 60},
    )
    size_chart.update_yaxes(title_text="Length (m)", secondary_y=False)
    size_chart.update_yaxes(title_text="Weight (kg)", secondary_y=True)
    st.plotly_chart(size_chart, width="stretch")

    show_insights([
        f"Average length: {average_length:.2f} m "
        f"(median {median_length:.2f} m).",
        f"Average weight: {average_weight:.2f} kg "
        f"(median {median_weight:.2f} kg).",
        f"Longest record: {longest['Observed Length (m)']:.2f} m; "
        f"heaviest: {heaviest['Observed Weight (kg)']:.2f} kg.",
    ])

left_column, right_column = st.columns(2)

with left_column:
    habitat_chart = px.bar(
        x=top_habitats.values,
        y=top_habitats.index.astype(str),
        orientation="h",
        text=top_habitats.values,
        labels={"x": "Observations", "y": "Habitat"},
        title="Top 5 Crocodile Habitats",
        color_discrete_sequence=[medium_green],
    )
    habitat_chart.update_traces(
        hovertemplate="%{y}<br>Observations: %{x:,}<extra></extra>",
        textposition="inside",
    )
    habitat_chart.update_layout(
        yaxis={"autorange": "reversed"},
        plot_bgcolor=plot_background,
        paper_bgcolor=background_green,
        font_color=text_green,
        showlegend=False,
    )
    st.plotly_chart(habitat_chart, width="stretch")

    top5_total = int(habitat_counts.loc[top_habitats.index].sum())
    show_insights([
        f"Most frequent habitat: {habitat_counts.index[0]} "
        f"({int(habitat_counts.iloc[0]):,} observations).",
        f"Top 5 habitats account for {top5_total:,} observations "
        f"({top5_total / total * 100:.1f}% of all observations).",
    ])

with right_column:
    status_chart = px.pie(
        values=cons_status.values,
        names=cons_status.index.astype(str),
        title="Conservation Status Distribution",
        color_discrete_sequence=green_palette,
        hole=0.15,
    )
    status_chart.update_traces(
        textposition="inside",
        textinfo="percent",
        hovertemplate="%{label}<br>%{value:,} observations (%{percent})<extra></extra>",
    )
    status_chart.update_layout(
        paper_bgcolor=background_green,
        font_color=text_green,
        legend={"font": {"color": text_green}},
    )
    st.plotly_chart(status_chart, width="stretch")

    show_insights([
        f"Most frequent recorded status: {cons_status.index[0]} "
        f"({int(cons_status.iloc[0]):,} observations, "
        f"{status_percentages.iloc[0]:.1f}%).",
        f"Distinct status categories: {cons_status.size}.",
    ])

st.subheader("Data quality")
quality_metrics = st.columns(4)
quality_metrics[0].metric("Rows", f"{len(df):,}")
quality_metrics[1].metric("Columns", f"{len(df.columns):,}")
quality_metrics[2].metric("Missing cells", f"{int(df.isna().sum().sum()):,}")
quality_metrics[3].metric("Duplicate rows", f"{int(df.duplicated().sum()):,}")

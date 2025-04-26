from preswald import text, plotly, connect, get_df, table, slider
import pandas as pd
import plotly.express as px

# Title and intro
text("# Welcome to Preswald!")
text("🌾 Exploring Crop Data from CSV")

# Step 1: Connect to Preswald and load the CSV
connect()
df = get_df('yield_1982')  # <-- your new csv name, without '.csv'

# Add a slider to filter by 'var'
min_var = slider(
    "Minimum Var Value",
    min_val=float(round(df['var'].min(), 2)),
    max_val=float(round(df['var'].max(), 2)),
    default=float(round(df['var'].min(), 2))
)

# Filter dataset
filtered_df = df[df['var'] >= min_var]

# 🔵 Live Counter showing number of points
text(f"✅ Currently displaying {len(filtered_df)} points based on selected var threshold.")

# Plot based on filtered data
if 'lon' in filtered_df.columns and 'lat' in filtered_df.columns:
    fig = px.scatter(
        filtered_df,
        x='lon',
        y='lat',
        color='var',
        title=f'🌾 Crop Distribution (var ≥ {min_var})',
        color_continuous_scale='Viridis',  # Color Theme
        labels={'lon': 'Longitude', 'lat': 'Latitude', 'var': 'Crop Variable'}
    )
    fig.update_layout(template="plotly_white")

    # Enhanced Hover
    fig.update_traces(
        hovertemplate="<br>".join([
            "Longitude: %{x}",
            "Latitude: %{y}",
            "Var: %{marker.color}"
        ])
    )

    plotly(fig)

# Show filtered data table
table(filtered_df, title=f"Filtered Crop Dataset (var ≥ {min_var})")


# 🌾 Crop Data Visualizer - Preswald App

This is a lightweight, interactive data app built using [Preswald](https://app.preswald.com/), a no-code/low-code platform for Python-backed UI applications.

The app loads agricultural crop yield data from a prepared `.csv` dataset and provides a dynamic, user-driven interface to explore crop distribution across the globe.

---

## 🚀 Features

- 📈 **Interactive Scatter Plot** of crop distribution (Longitude vs Latitude)
- 🎚️ **Dynamic Slider** to filter data based on `var` threshold (live updates to plot and table)
- 🎨 **Customized Color Themes** (`Viridis`, `Plasma`, etc.) for enhanced visualization
- 🔍 **Zoom and Pan** capabilities built-in with Plotly for map exploration
- 🛠️ **Enhanced Hover Tooltips** showing Longitude, Latitude, and Variable Value
- 📋 **Dynamic Table View** of filtered data
- 🔥 **Live Point Counter** displaying currently active data points

---

## 🧠 Tech Stack

- **Preswald SDK** (Python no-code/low-code app builder)
- **Plotly Express** for visualization
- **Pandas** for data manipulation
- **Interactive UI widgets** (slider, table, text)

---

## 📂 Project Structure

```bash
data/
 ├── yield_1982.csv    # Final cleaned dataset
images/
 ├── favicon.ico                        # App favicon (optional)
 ├── logo.png                           # App logo (optional)
scripts/
 ├── main.py                             # App logic: loading, filtering, plotting
preswald.toml                            # App branding and config
README.md                                # (This file)

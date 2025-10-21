# 📈 Indian Stock Market Dashboard

An interactive Streamlit dashboard showcasing Indian stock market data, charts, technical indicators, and simple future price predictions. Built for demonstration and educational purposes.

## ✨ Key features

- 🔎 Real-time and historical price visualization using Yahoo Finance (`yfinance`).
- 📊 Interactive Plotly charts (candlestick, volume, prediction overlays).
- 🧮 Technical indicators: moving averages, RSI, Bollinger Bands.
- 🤖 Simple ensemble-based prediction fallback (RandomForest + trend models). LSTM helper code included.
- 🔐 User authentication (local JSON storage) with registration and login UI.
- 🎨 Clean, glassmorphism-inspired UI components and custom CSS.

## ⚙️ Prerequisites

- Python 3.10+ (tested with 3.10 — newer versions should work).
- On Windows, a standard Command Prompt (`cmd.exe`) is used in the examples below.

## 🛠️ Installation

1. Clone or copy the project to your machine.

2. From the project root directory (where `requirements.txt` lives), create and activate a virtual environment (recommended):

```bat
python -m venv .venv
.venv\Scripts\activate
```

3. Install required Python packages:

```bat
python -m pip install -r requirements.txt
```

> ⚠️ Note: The repository's `requirements.txt` includes heavy packages (e.g. TensorFlow). If you only want the interactive dashboard without training models locally, consider creating a lighter requirements file that omits ML-specific packages.

## ▶️ Running the dashboard

There are two easy ways to run the app.

1) Use the included startup helper (recommended):

```bat
python run_dashboard.py
```

This script will attempt to install requirements (if not already present) and then start Streamlit on port 8501.

2) Run Streamlit directly:

```bat
streamlit run main.py --server.port=8501
```

Then open `http://localhost:8501` in your browser.

## 📁 Project layout

- `main.py` — Streamlit app entrypoint and application flow (authentication, navigation, pages).
- `run_dashboard.py` — Helper script to install requirements and launch the Streamlit app.
- `requirements.txt` — Python dependencies used by the project.
- `users.json` — Local JSON file used for storing simple user accounts (created at runtime).
- `components/` — UI and authentication components:
  - `auth.py` — Authentication UI and user management (local JSON storage).
  - `ui_components.py` — Custom UI helpers and Plotly chart builders.
- `pages/` — Dashboard page definitions and content sections.
- `utils/` — Support utilities:
  - `stock_data.py` — Data fetching and caching using `yfinance`.
  - `prediction_model.py` — Prediction utilities (RandomForest/Linear trend and LSTM scaffolding).

## 📌 Usage notes & tips

- ⚠️ The authentication system stores user data in `users.json` in the project directory. This is for demo only — do not use in production.
- 🔍 Predictions provided by `PredictionModel` are illustrative and should not be used for financial decisions.
- 🔁 If you plan to deploy or share the app, remove any automatic pip-install behavior and pin package versions appropriately.

## 🛟 Troubleshooting

- ❗ If Streamlit fails to start, ensure your virtual environment is activated and dependencies are installed.
- 🌐 If `yfinance` returns empty data for a ticker, check your internet connection and the ticker symbol (NSE tickers use the `.NS` suffix, e.g. `RELIANCE.NS`).
- 🪟 On Windows, if the `streamlit` command is not found after installing requirements, ensure your environment's `Scripts` directory is on PATH or use `python -m streamlit run main.py`.

## 🤝 Contributing

- This project is intended as an educational demo. Contributions are welcome — please open issues or pull requests with focused changes (bug fixes, doc updates, small features).

---

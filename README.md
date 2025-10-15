# Indian Stock Market Dashboard 📈🇮🇳

A beautiful, real-time stock market dashboard for Indian stocks with glassmorphism UI, user authentication, and ML-powered price predictions up to 2030. 🚀

## Features ✨

- **🔐 User Authentication**: Secure login/register system
- **🌓 Dark/Light Mode**: Animated theme toggle
- **💎 Glassmorphism UI**: Beautiful frosted glass effects with gradient colors
- **🔄 Card Flip Animations**: Interactive card components with flip effects
- **📊 Real-time Stock Data**: Live Indian stock market data using yfinance API
- **📈 Interactive Charts**: Candlestick charts, volume charts, and technical indicators
- **🔮 Future Predictions**: ML-powered stock price predictions up to 2030
- **📱 Responsive Design**: Mobile-friendly responsive layout
- **🎯 Technical Analysis**: RSI, MACD, Bollinger Bands, and more
- **🏦 Market Overview**: Top gainers/losers, sector performance, market indices

## Technologies Used 🛠️

- **Frontend**: Streamlit with custom CSS
- **Data**: yfinance API for Indian stock market data
- **Visualization**: Plotly for interactive charts
- **ML/AI**: TensorFlow/Keras LSTM, Random Forest, Linear Regression
- **Data Processing**: Pandas, NumPy
- **Authentication**: Custom authentication system with session management

## Installation & Setup 🚀

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KGFCH2/India_Stock_Dashboard.git
   cd India_Stock_Dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**:
   ```bash
   python run_dashboard.py
   ```
   
   Or manually:
   ```bash
   streamlit run main.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

### Alternative Installation
You can also use the startup script which will automatically install dependencies:
```bash
python run_dashboard.py
# Indian Stock Market Dashboard 📈

A Streamlit-based dashboard that displays real-time Indian stock market data, interactive charts, basic user authentication, and ML-backed price predictions for exploration and educational purposes.

This README provides a complete guide to setup, run, develop, and extend the project.

## Table of contents

- [Demo & screenshots](#demo--screenshots)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Quick start (Windows, macOS, Linux)](#quick-start-windows-macos-linux)
- [Project structure](#project-structure)
- [Development notes](#development-notes)
- [Testing & linting](#testing--linting)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Demo & screenshots

Place screenshots or a short demo GIF in `/static/` and reference them here. Example:

![Dashboard screenshot](static/dashboard_preview.png)

If you'd like, I can add example screenshots to the repo.

## Features

- Real-time stock quotations (via `yfinance`)
- Interactive Plotly charts (candlestick, volume, moving averages)
- Technical indicators: RSI, MACD, Bollinger Bands
- Local user authentication (stored in `users.json`) for demo purposes
- Theme toggle (dark/light) and glassmorphism UI
- ML prediction utilities (LSTM / Random Forest / Linear Regression) in `utils/prediction_model.py`

## Tech stack

- Python 3.8+
- Streamlit for UI
- yfinance for market data
- Plotly for charts
- Pandas / NumPy for data processing
- TensorFlow / scikit-learn for models (optional, local)

## Quick start (Windows, macOS, Linux)

These steps get the project running locally.

1. Clone the repository

```cmd
git clone https://github.com/KGFCH2/India_Stock_Dashboard.git
cd "India_Stock_Dashboard"
```

2. Create and activate a virtual environment (recommended)

Windows (cmd.exe):

```cmd
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux (bash/zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Upgrade pip and install dependencies

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the dashboard

Recommended (uses `run_dashboard.py` helper):

```cmd
python run_dashboard.py
```

Or directly with Streamlit:

```cmd
streamlit run main.py
```

Then open http://localhost:8501 in your browser.

Notes:
- If `run_dashboard.py` fails to install optional ML packages, install them separately (see `requirements.txt`).
- The app stores user data in `users.json` (local demo only) — do not use this for production authentication.

## Project structure

Top-level files and folders:

```
India_Stock_Dashboard/
├── components/         # UI helpers and authentication (auth.py, ui_components.py)
├── pages/              # Streamlit pages (dashboard_pages.py)
├── utils/              # Data fetching and ML helpers (stock_data.py, prediction_model.py)
├── static/             # Images and static assets (optional)
├── main.py             # Streamlit app entry point
├── run_dashboard.py    # Helper to install deps and run the app
├── requirements.txt    # Python dependencies
├── users.json          # Local user datastore (demo)
├── README.md
└── LICENSE
```

Files of interest:

- `components/auth.py` — simple register/login functions using `users.json`.
- `components/ui_components.py` — reusable UI blocks and CSS injection.
- `pages/dashboard_pages.py` — the main pages for market overview, portfolio, news, analytics.
- `utils/stock_data.py` — wrappers around `yfinance` and preprocessing utilities.
- `utils/prediction_model.py` — model training/forecast helpers (can be heavy).

## Development notes

- Keep `requirements.txt` up-to-date when adding packages.
- Use a virtual environment to avoid dependency conflicts.
- ML model code is optional; heavy training should be done offline and models saved to disk.

Running locally during development

```cmd
# activate your venv first
streamlit run main.py
```

Adding a new page

Create a new function in `pages/dashboard_pages.py` and import/use it from `main.py` where Streamlit constructs the navigation.

Example skeleton for a new page (add to `pages/dashboard_pages.py`):

```python
def show_routes():
   st.markdown('# Routes')
   routes = [
      {'id':'E-1','name':'Express 1'},
      {'id':'AC-1','name':'AC Route 1'},
      {'id':'SD-3','name':'Shuttle 3'},
   ]
   q = st.text_input('Filter routes (search by id or name)')
   if q:
      routes = [r for r in routes if q.lower() in r['id'].lower() or q.lower() in r['name'].lower()]
   for r in routes:
      st.write(f"{r['id']} — {r['name']}")
```

I can add a `Routes` page and the filter input for you if you'd like — tell me whether to create `pages/routes.py` or add it to `pages/dashboard_pages.py`.

## Testing & linting

- There are no automated tests by default. Adding `pytest` and a few smoke tests is recommended.
- For Python linting, use `flake8` or `pylint` and configure pre-commit hooks.

## Troubleshooting

- If Streamlit fails to start, ensure the virtual environment is activated and `requirements.txt` was installed.
- If data calls fail, check your network or yfinance rate limits.
- If UI looks broken, clear Streamlit cache: `streamlit cache clear` (or delete `.streamlit` session files).

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and add tests where appropriate
4. Commit and push: `git commit -am "Add feature" && git push origin feature/my-feature`
5. Open a Pull Request describing your change

---

### 📚 Educational Purpose Disclaimer

This demonstration is for educational purposes only.
Built for project demonstration and learning purposes.
Not intended for actual investment decisions. Please consult financial advisors for investment advice.

🇮🇳 Made with ❤️ for Indian Stock Market Learning

---
# Indian Stock Market Dashboard 📈

A beautiful, real-time stock market dashboard for Indian stocks with glassmorphism UI, user authentication, and ML-powered price predictions up to 2030.

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
```

## Project Structure 📁

```
India_Stock_Dashboard/
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── components/             # Core application components
│   ├── auth.py            # Authentication system
│   ├── ui_components.py   # UI components and styling
│   └── __init__.py
├── pages/                 # Dashboard pages
│   ├── dashboard_pages.py # Additional dashboard pages
│   └── __init__.py
├── utils/                 # Utility modules
│   ├── stock_data.py     # Stock data fetching and processing
│   ├── prediction_model.py # ML prediction models
│   └── __init__.py
├── main.py               # Main application entry point
├── run_dashboard.py      # Startup script with auto-install
├── requirements.txt      # Python dependencies
├── users.json           # User data storage
├── LICENSE              # MIT License
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```
├── run_dashboard.py       # Startup script
│
├── components/
│   ├── auth.py            # Authentication system
│   └── ui_components.py   # UI components and styling
│
├── utils/
│   ├── stock_data.py      # Stock data fetching utilities
│   └── prediction_model.py # ML prediction models
│
├── pages/
│   └── dashboard_pages.py # Additional dashboard pages
│
├── .streamlit/
│   └── config.toml        # Streamlit configuration
│
└── static/                # Static assets (if any)
```

## Usage Guide 📖

### 1. Authentication
- Create a new account or login with existing credentials
- User data is stored locally in `users.json`

### 2. Stock Selection
- Use the sidebar to select from popular Indian stocks
- Choose time periods (1D to 5Y) for analysis

### 3. Dashboard Features
- **Stock Cards**: Flip cards showing current price, change, volume, and market cap
- **Price Charts**: Interactive candlestick charts with moving averages
- **Volume Analysis**: Volume charts with color-coded bars
- **Technical Indicators**: RSI, Bollinger Bands, and more
- **Future Predictions**: ML-powered price forecasts

### 4. Theme Toggle
- Click the theme toggle button to switch between dark/light modes
- Glassmorphism effects adapt to the selected theme

## Stock Prediction Models 🤖

The dashboard uses multiple ML approaches:

1. **LSTM Neural Networks**: For complex time series patterns
2. **Random Forest**: For feature-based predictions
3. **Linear Regression**: For trend analysis
4. **Ensemble Methods**: Combining multiple models for better accuracy

## Supported Indian Stocks 🇮🇳

- Reliance Industries (RELIANCE.NS)
- Tata Consultancy Services (TCS.NS)
- HDFC Bank (HDFCBANK.NS)
- Infosys (INFY.NS)
- ICICI Bank (ICICIBANK.NS)
- State Bank of India (SBIN.NS)
- Bharti Airtel (BHARTIARTL.NS)
- ITC Limited (ITC.NS)
- Kotak Mahindra Bank (KOTAKBANK.NS)
- Hindustan Unilever (HINDUNILVR.NS)
- And many more...

## Technical Indicators 📊

- **Moving Averages**: SMA, EMA (20, 50, 200 periods)
- **RSI**: Relative Strength Index (14 periods)
- **MACD**: Moving Average Convergence Divergence
- **Bollinger Bands**: With 2 standard deviations
- **Volume Analysis**: Volume SMA and ratios

## Future Enhancements 🔮

- Portfolio tracking and management
- Real-time alerts and notifications
- News sentiment analysis
- Options and derivatives data
- Screener for stock filtering
- Social trading features
- Mobile app version

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer ⚠️

This dashboard is for educational and informational purposes only. Stock predictions are based on historical data and machine learning models, which may not be accurate. Always do your own research and consult with financial advisors before making investment decisions.

## Support 💬

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Made with ❤️ for Indian Stock Market Enthusiasts**
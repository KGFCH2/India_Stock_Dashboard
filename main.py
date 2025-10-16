import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import yfinance as yf
import numpy as np
import json
import hashlib
import time

# Page configuration
st.set_page_config(
    page_title="Indian Stock Market Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import custom components
from components.auth import Authentication
from components.ui_components import UIComponents
from utils.stock_data import StockDataFetcher
from utils.prediction_model import PredictionModel
from pages.dashboard_pages import show_market_overview, show_portfolio, show_news, show_analytics

class StockDashboard:
    def __init__(self):
        self.auth = Authentication()
        self.ui = UIComponents()
        self.stock_fetcher = StockDataFetcher()
        self.predictor = PredictionModel()
        
        # Initialize session state
        if 'theme' not in st.session_state:
            st.session_state.theme = 'light'
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'username' not in st.session_state:
            st.session_state.username = None

    def run(self):
        """Main application runner"""
        # Apply CSS styling
        self.ui.apply_custom_css()
        # Inline override: force transparency on buttons (runs after component CSS)
        st.markdown("""
        <style>
        button[style*="linear-gradient"], .stButton > button, .stButton > button[data-testid*="top_nav_"], .stButton > button[data-testid*="nav_"] {
            background-image: none !important;
            background-color: transparent !important;
            background: transparent !important;
            color: #0b2545 !important;
            border: 1px solid rgba(0,0,0,0.08) !important;
            box-shadow: none !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Authentication check
        if not st.session_state.authenticated:
            self.auth.show_auth_page()
        else:
            self.show_main_dashboard()

    def show_main_dashboard(self):
        """Display the main dashboard"""
        # Welcome message
        st.markdown(f'<h3 class="gradient-text">Welcome, {st.session_state.username}! <span class="emoji-normal">👋</span></h3>', unsafe_allow_html=True)
        
        # Main title
        st.markdown('<h1><span class="emoji-normal">📈</span> <span class="gradient-title">Indian Stock Market Dashboard</span></h1>', unsafe_allow_html=True)
        
        # Separate navigation bar for main actions
        st.markdown('''
        <div class="nav-bar">
            <div style="display: flex; gap: 15px; align-items: center;">
        ''', unsafe_allow_html=True)
        
        # Create navigation with Logout on the right (Analytics removed)
        left_col, middle_col, right_col = st.columns([4, 1, 1])

        with left_col:
            # left area intentionally empty
            st.markdown("<div style='height:1px'></div>", unsafe_allow_html=True)

        with middle_col:
            # placeholder for spacing
            st.markdown("<div style='height:1px'></div>", unsafe_allow_html=True)

        with right_col:
            if st.button("🚪 Logout", key="top_nav_logout", help="Logout", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.username = None
                st.rerun()

        st.markdown('</div></div>', unsafe_allow_html=True)

        # Navigation menu
        menu_options = {
            "🏠 Dashboard": "dashboard",
            "🏦 Market Overview": "market",
            "💼 Portfolio": "portfolio",
            "📰 News": "news",
            "📊 Analytics": "analytics"
        }
        
        # Initialize page selection
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'dashboard'
        
        # Create navigation buttons
        cols = st.columns(len(menu_options))
        for i, (label, page_key) in enumerate(menu_options.items()):
            with cols[i]:
                if st.button(label, key=f"nav_{page_key}"):
                    st.session_state.current_page = page_key
                    st.rerun()
        
        st.markdown("---")
        
        # Display selected page content
        if st.session_state.current_page == 'dashboard':
            # Sidebar for stock selection (only show on dashboard page)
            self.show_sidebar()
            self.show_dashboard_content()
        elif st.session_state.current_page == 'market':
            show_market_overview()
        elif st.session_state.current_page == 'portfolio':
            show_portfolio()
        elif st.session_state.current_page == 'news':
            show_news()
        elif st.session_state.current_page == 'analytics':
            show_analytics()
        
        # Add educational disclaimer at the bottom
        self.ui.display_educational_disclaimer()

    def show_sidebar(self):
        """Sidebar with stock selection and filters"""
        st.sidebar.markdown('<h2 class="gradient-text">🔍 Stock Selection</h2>', unsafe_allow_html=True)
        
        # Popular Indian stocks
        indian_stocks = {
            "Reliance Industries": "RELIANCE.NS",
            "Tata Consultancy Services": "TCS.NS", 
            "HDFC Bank": "HDFCBANK.NS",
            "Infosys": "INFY.NS",
            "ICICI Bank": "ICICIBANK.NS",
            "State Bank of India": "SBIN.NS",
            "Bharti Airtel": "BHARTIARTL.NS",
            "ITC Limited": "ITC.NS",
            "Kotak Mahindra Bank": "KOTAKBANK.NS",
            "Hindustan Unilever": "HINDUNILVR.NS"
        }
        
        selected_stock_name = st.sidebar.selectbox(
            "Select Stock",
            options=list(indian_stocks.keys()),
            index=0
        )
        
        st.session_state.selected_stock = indian_stocks[selected_stock_name]
        st.session_state.selected_stock_name = selected_stock_name
        
        # Time period selection
        time_periods = {
            "1 Day": "1d",
            "5 Days": "5d", 
            "1 Month": "1mo",
            "3 Months": "3mo",
            "6 Months": "6mo",
            "1 Year": "1y",
            "2 Years": "2y",
            "5 Years": "5y"
        }
        
        selected_period_name = st.sidebar.selectbox(
            "Time Period",
            options=list(time_periods.keys()),
            index=3
        )
        
        st.session_state.time_period = time_periods[selected_period_name]
        
        # Auto-refresh toggle
        auto_refresh = st.sidebar.checkbox("🔄 Auto Refresh (30s)", value=False)
        
        if auto_refresh:
            time.sleep(30)
            st.rerun()

    def show_dashboard_content(self):
        """Main dashboard content area"""
        # Get stock data
        try:
            stock_data = self.stock_fetcher.get_stock_data(
                st.session_state.selected_stock,
                st.session_state.time_period
            )
            
            if stock_data is not None and not stock_data.empty:
                # Stock info cards
                self.ui.display_stock_cards(stock_data, st.session_state.selected_stock_name)
                
                # Charts section
                col1, col2 = st.columns(2)
                
                with col1:
                    # Price chart
                    fig_price = self.ui.create_price_chart(stock_data, st.session_state.selected_stock_name)
                    st.plotly_chart(fig_price, use_container_width=True)
                
                with col2:
                    # Volume chart
                    fig_volume = self.ui.create_volume_chart(stock_data, st.session_state.selected_stock_name)
                    st.plotly_chart(fig_volume, use_container_width=True)
                
                # Technical indicators
                self.ui.display_technical_indicators(stock_data)
                
                # Future predictions
                self.show_predictions(stock_data)
                
            else:
                st.error("Failed to fetch stock data. Please try again.")
                
        except Exception as e:
            st.error(f"Error loading stock data: {str(e)}")

        # predictions are generated and displayed in show_predictions()

    def show_predictions(self, stock_data):
        """Display future price predictions"""
        try:
            predictions = self.predictor.predict_future_prices(
                stock_data,
                st.session_state.selected_stock,
                years_ahead=5
            )

            if predictions is not None:
                fig_prediction = self.ui.create_prediction_chart(
                    stock_data,
                    predictions,
                    st.session_state.selected_stock_name
                )
                st.plotly_chart(fig_prediction, use_container_width=True)
                # Prediction summary
                self.ui.display_prediction_summary(predictions)
            else:
                st.warning("Unable to generate predictions at this time.")

        except Exception as e:
            st.error(f"Error generating predictions: {str(e)}")

if __name__ == "__main__":
    app = StockDashboard()
    app.run()
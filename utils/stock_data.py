import yfinance as yf
import pandas as pd
import requests
import streamlit as st
from datetime import datetime, timedelta
import time
import numpy as np

class StockDataFetcher:
    def __init__(self):
        self.cache_duration = 300  # 5 minutes cache
        self.last_fetch = {}
        self.cached_data = {}
    
    def get_stock_data(self, symbol, period="1mo"):
        """Fetch stock data with caching"""
        cache_key = f"{symbol}_{period}"
        current_time = time.time()
        
        # Check if we have cached data that's still fresh
        if (cache_key in self.cached_data and 
            cache_key in self.last_fetch and 
            current_time - self.last_fetch[cache_key] < self.cache_duration):
            return self.cached_data[cache_key]
        
        try:
            # Create ticker object
            ticker = yf.Ticker(symbol)
            
            # Fetch historical data
            data = ticker.history(period=period)
            
            if data.empty:
                st.error(f"No data found for symbol: {symbol}")
                return None
            
            # Cache the data
            self.cached_data[cache_key] = data
            self.last_fetch[cache_key] = current_time
            
            return data
            
        except Exception as e:
            st.error(f"Error fetching data for {symbol}: {str(e)}")
            return None
    
    def get_real_time_price(self, symbol):
        """Get real-time price for a stock"""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period="1d", interval="1m")
            
            if not data.empty:
                return data['Close'].iloc[-1]
            else:
                return None
                
        except Exception as e:
            st.error(f"Error fetching real-time price for {symbol}: {str(e)}")
            return None
    
    def get_stock_info(self, symbol):
        """Get detailed stock information"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return info
        except Exception as e:
            st.error(f"Error fetching stock info for {symbol}: {str(e)}")
            return {}
    
    def get_multiple_stocks_data(self, symbols, period="1mo"):
        """Fetch data for multiple stocks"""
        stocks_data = {}
        
        for symbol in symbols:
            data = self.get_stock_data(symbol, period)
            if data is not None:
                stocks_data[symbol] = data
        
        return stocks_data
    
    def get_indian_market_indices(self):
        """Get major Indian market indices"""
        indices = {
            "NIFTY 50": "^NSEI",
            "SENSEX": "^BSESN", 
            "NIFTY BANK": "^NSEBANK",
            "NIFTY IT": "^CNXIT",
            "NIFTY AUTO": "^CNXAUTO"
        }
        
        indices_data = {}
        
        for name, symbol in indices.items():
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period="1d")
                if not data.empty:
                    current_price = data['Close'].iloc[-1]
                    prev_close = data['Close'].iloc[-2] if len(data) > 1 else current_price
                    change = current_price - prev_close
                    change_pct = (change / prev_close) * 100 if prev_close != 0 else 0
                    
                    indices_data[name] = {
                        'price': current_price,
                        'change': change,
                        'change_pct': change_pct
                    }
            except Exception as e:
                st.warning(f"Could not fetch data for {name}: {str(e)}")
        
        return indices_data
    
    def get_top_gainers_losers(self):
        """Get top gainers and losers from Indian market"""
        # Popular Indian stocks for analysis
        indian_stocks = [
            "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
            "SBIN.NS", "BHARTIARTL.NS", "ITC.NS", "KOTAKBANK.NS", "HINDUNILVR.NS",
            "LT.NS", "AXISBANK.NS", "MARUTI.NS", "ASIANPAINT.NS", "WIPRO.NS"
        ]
        
        stocks_performance = []
        
        for symbol in indian_stocks:
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period="2d")
                
                if len(data) >= 2:
                    current_price = data['Close'].iloc[-1]
                    prev_price = data['Close'].iloc[-2]
                    change_pct = ((current_price - prev_price) / prev_price) * 100
                    
                    stocks_performance.append({
                        'symbol': symbol,
                        'name': symbol.replace('.NS', ''),
                        'current_price': current_price,
                        'change_pct': change_pct
                    })
            except:
                continue
        
        # Sort by performance
        stocks_performance.sort(key=lambda x: x['change_pct'], reverse=True)
        
        gainers = stocks_performance[:5]  # Top 5 gainers
        losers = stocks_performance[-5:]  # Top 5 losers
        
        return gainers, losers
    
    def get_sector_performance(self):
        """Get sector-wise performance"""
        sectors = {
            "Banking": ["HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "KOTAKBANK.NS", "AXISBANK.NS"],
            "IT": ["TCS.NS", "INFY.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS"],
            "Auto": ["MARUTI.NS", "M&M.NS", "TATAMOTORS.NS", "BAJAJ-AUTO.NS", "HEROMOTOCO.NS"],
            "Pharma": ["SUNPHARMA.NS", "DRREDDY.NS", "CIPLA.NS", "DIVISLAB.NS", "LUPIN.NS"],
            "FMCG": ["HINDUNILVR.NS", "ITC.NS", "NESTLEIND.NS", "BRITANNIA.NS", "DABUR.NS"]
        }
        
        sector_performance = {}
        
        for sector, stocks in sectors.items():
            sector_changes = []
            
            for stock in stocks:
                try:
                    ticker = yf.Ticker(stock)
                    data = ticker.history(period="2d")
                    
                    if len(data) >= 2:
                        current_price = data['Close'].iloc[-1]
                        prev_price = data['Close'].iloc[-2]
                        change_pct = ((current_price - prev_price) / prev_price) * 100
                        sector_changes.append(change_pct)
                except:
                    continue
            
            if sector_changes:
                avg_change = np.mean(sector_changes)
                sector_performance[sector] = avg_change
        
        return sector_performance
    
    def get_market_news(self):
        """Get latest market news (placeholder - would need news API)"""
        # This is a placeholder. In a real application, you would integrate with news APIs
        sample_news = [
            {
                "title": "Indian Markets Show Strong Performance",
                "summary": "NIFTY and SENSEX both gained significantly today...",
                "time": "2 hours ago"
            },
            {
                "title": "Tech Stocks Rally Continues", 
                "summary": "IT sector shows strong momentum with TCS and Infosys leading...",
                "time": "4 hours ago"
            },
            {
                "title": "Banking Sector Mixed Performance",
                "summary": "While HDFC Bank gained, some PSU banks showed weakness...",
                "time": "6 hours ago"
            }
        ]
        
        return sample_news
    
    def calculate_technical_indicators(self, data):
        """Calculate various technical indicators"""
        if data.empty:
            return {}
        
        indicators = {}
        
        # Moving Averages
        indicators['SMA_20'] = data['Close'].rolling(window=20).mean()
        indicators['SMA_50'] = data['Close'].rolling(window=50).mean()
        indicators['EMA_12'] = data['Close'].ewm(span=12).mean()
        indicators['EMA_26'] = data['Close'].ewm(span=26).mean()
        
        # RSI
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        indicators['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        indicators['MACD'] = indicators['EMA_12'] - indicators['EMA_26']
        indicators['MACD_signal'] = indicators['MACD'].ewm(span=9).mean()
        indicators['MACD_histogram'] = indicators['MACD'] - indicators['MACD_signal']
        
        # Bollinger Bands
        sma_20 = indicators['SMA_20']
        std_20 = data['Close'].rolling(window=20).std()
        indicators['BB_upper'] = sma_20 + (std_20 * 2)
        indicators['BB_lower'] = sma_20 - (std_20 * 2)
        
        # Volume indicators
        indicators['Volume_SMA'] = data['Volume'].rolling(window=20).mean()
        
        return indicators
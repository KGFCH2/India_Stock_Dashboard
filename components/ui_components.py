import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import pandas as pd

class UIComponents:
    def __init__(self):
        self.current_theme = st.session_state.get('theme', 'dark')
    
    def apply_custom_css(self):
        """Apply custom CSS for glassmorphism design"""
        theme = st.session_state.get('theme', 'dark')
        
        if theme == 'dark':
            background_gradient = "linear-gradient(135deg, #FF9933 0%, #FFFFFF 50%, #138808 100%)"
            card_bg = "rgba(0, 0, 0, 0.3)"
            text_color = "transparent"  # Will use gradient text classes
            border_color = "rgba(255, 255, 255, 0.3)"
        else:
            background_gradient = "linear-gradient(135deg, #FF9933 0%, #FFFFFF 50%, #138808 100%)"
            card_bg = "rgba(255, 255, 255, 0.4)"
            text_color = "transparent"  # Will use gradient text classes
            border_color = "rgba(0, 0, 0, 0.2)"
        
        css = f"""
        <style>
        /* Main background */
        .stApp {{
            background: {background_gradient};
        }}
        
        /* Simple text styling for headings */
        h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {{
            background: linear-gradient(90deg, rgb(22, 160, 133), rgb(52, 152, 219));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            font-weight: bold;
        }}
        
        /* Simple regular text */
        .stApp p, .stApp div, .stApp span {{
            color: #2c3e50;
            font-weight: 500;
        }}
        
        /* Glassmorphism cards */
        .glass-card {{
            background: {card_bg};
            backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 1px solid {border_color};
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            transition: all 0.3s ease;
        }}
        
        .glass-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 40px 0 rgba(31, 38, 135, 0.5);
        }}
        
        /* Flip card animation - Fixed and Enhanced */
        .flip-card {{
            background-color: transparent;
            width: 100%;
            height: 220px;
            perspective: 1000px;
            margin: 15px 0;
            cursor: pointer;
        }}
        
        .flip-card-inner {{
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s ease-in-out;
            transform-style: preserve-3d;
        }}
        
        .flip-card:hover .flip-card-inner {{
            transform: rotateY(180deg);
        }}
        
        .flip-card-front, .flip-card-back {{
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        
        .flip-card-front {{
            background: linear-gradient(135deg, rgba(22, 160, 133, 0.1), rgba(52, 152, 219, 0.1));
        }}
        
        .flip-card-back {{
            transform: rotateY(180deg);
            background: linear-gradient(135deg, rgba(255, 153, 51, 0.1), rgba(19, 136, 8, 0.1));
        }}
        
        /* Enhanced flip card content */
        .flip-card h3, .flip-card h4 {{
            margin: 0 0 10px 0;
            font-size: 1.2rem;
        }}
        
        .flip-card .metric-value {{
            font-size: 2rem;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .flip-card .metric-label {{
            font-size: 0.9rem;
            opacity: 0.8;
        }}
        
        .flip-card-back p {{
            margin: 5px 0;
            font-size: 1rem;
            color: #2c3e50;
            font-weight: 500;
        }}
        
        /* Simple gradient text with green+blue combination */
        .gradient-text {{
            background: linear-gradient(90deg, rgb(22, 160, 133), rgb(52, 152, 219));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            font-weight: bold;
        }}
        
        /* Ensure emojis are never affected by gradients */
        .emoji-normal {{
            background: none !important;
            -webkit-background-clip: initial !important;
            -webkit-text-fill-color: initial !important;
            background-clip: initial !important;
            color: initial !important;
            display: inline-block;
            margin-right: 8px;
        }}
        
        /* Navigation bar styling */
        .nav-bar {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 10px 20px;
            margin: 10px 0;
            display: flex;
            justify-content: flex-end;
            gap: 15px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }}
        
        .nav-button {{
            background: rgba(255, 255, 255, 0.9) !important;
            color: #2c3e50 !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 8px 16px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            cursor: pointer !important;
        }}
        
        .nav-button:hover {{
            background: rgba(255, 255, 255, 1) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        }}
        
        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        /* Simple gradient text for titles */
        .gradient-title {{
            background: linear-gradient(90deg, rgb(22, 160, 133), rgb(52, 152, 219));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            font-weight: 900;
            font-size: 2.5rem;
            letter-spacing: -0.02em;
            line-height: 1.1;
        }}
        
        /* Simple gradient text for labels */
        .gradient-label {{
            background: linear-gradient(135deg, rgb(39, 174, 96), rgb(52, 152, 219));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            font-weight: 600;
        }}
        
        /* Simple Streamlit elements */
        .stSelectbox label, .stTextInput label, .stNumberInput label, .stDateInput label {{
            color: #2c3e50;
            font-weight: 600;
        }}
        
        /* Simple sidebar text */
        .css-1d391kg p, .css-1d391kg span, .css-1d391kg div {{
            color: #2c3e50;
            font-weight: 500;
        }}
        
        /* Simple button styling with clear background */
        .stButton > button {{
            background: rgba(255, 255, 255, 0.9) !important;
            border: 2px solid #2c3e50 !important;
            border-radius: 8px !important;
            color: #2c3e50 !important;
            font-weight: bold !important;
            padding: 0.5rem 1rem !important;
            transition: all 0.3s ease !important;
        }}
        
        /* Navigation button specific styling */
        .stButton > button[data-testid*="top_nav_"] {{
            background: rgba(255, 255, 255, 0.95) !important;
            border: 1px solid rgba(22, 160, 133, 0.3) !important;
            border-radius: 10px !important;
            color: #2c3e50 !important;
            font-weight: 600 !important;
            padding: 8px 16px !important;
            margin: 2px !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
        }}
        
        .stButton > button[data-testid*="top_nav_"]:hover {{
            background: rgba(255, 255, 255, 1) !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15) !important;
            border-color: rgba(22, 160, 133, 0.5) !important;
        }}
        
        .stButton > button:hover {{
            background: rgba(255, 255, 255, 1) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(44, 62, 80, 0.3) !important;
        }}
        
        /* Simple button text */
        .stButton button span {{
            color: #2c3e50 !important;
            font-weight: bold !important;
        }}
        
        /* Metric cards */
        .metric-card {{
            background: {card_bg};
            backdrop-filter: blur(20px);
            border-radius: 15px;
            border: 1px solid {border_color};
            padding: 15px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }}
        
        .metric-card:hover {{
            transform: scale(1.05);
        }}
        
        .metric-value {{
            font-size: 2rem;
            font-weight: bold;
            background: linear-gradient(90deg, rgb(22, 160, 133), rgb(52, 152, 219));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
        }}
        
        .metric-label {{
            font-size: 0.9rem;
            color: #34495e;
            font-weight: 600;
            margin-top: 5px;
        }}
        
        /* Simple theme toggle button */
        .theme-toggle {{
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
            border-radius: 50px;
            color: white;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }}
        
        .theme-toggle:hover {{
            transform: scale(1.1);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }}
        
        /* Sidebar styling */
        .css-1d391kg {{
            background: {card_bg};
            backdrop-filter: blur(20px);
        }}
        
        /* Custom selectbox */
        .stSelectbox > div > div {{
            background: {card_bg};
            backdrop-filter: blur(10px);
            border-radius: 10px;
            border: 1px solid {border_color};
        }}
        
        /* Loading animation */
        .loading-spinner {{
            border: 4px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top: 4px solid #ff6b6b;
            width: 40px;
            height: 40px;
            animation: spin 2s linear infinite;
            margin: 20px auto;
        }}
        
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        /* Price change indicators */
        .price-up {{
            color: #00ff88;
            font-weight: bold;
        }}
        
        .price-down {{
            color: #ff4757;
            font-weight: bold;
        }}
        
        .price-neutral {{
            color: #ffa502;
            font-weight: bold;
        }}
        </style>
        """
        
        st.markdown(css, unsafe_allow_html=True)
    
    def display_stock_cards(self, stock_data, stock_name):
        """Display stock information in flip cards"""
        current_price = stock_data['Close'].iloc[-1]
        prev_price = stock_data['Close'].iloc[-2] if len(stock_data) > 1 else current_price
        price_change = current_price - prev_price
        price_change_pct = (price_change / prev_price) * 100 if prev_price != 0 else 0
        
        # Determine price change color
        if price_change > 0:
            change_class = "price-up"
            change_icon = "📈"
        elif price_change < 0:
            change_class = "price-down"
            change_icon = "📉"
        else:
            change_class = "price-neutral"
            change_icon = "➡️"
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h3 class="gradient-text">Current Price</h3>
                        <div class="metric-value {change_class}">₹{current_price:.2f}</div>
                        <div class="metric-label gradient-label">{stock_name}</div>
                    </div>
                    <div class="flip-card-back">
                        <h4><span class="gradient-text">Price Details</span></h4>
                        <p><strong>Open:</strong> ₹{stock_data['Open'].iloc[-1]:.2f}</p>
                        <p><strong>High:</strong> ₹{stock_data['High'].iloc[-1]:.2f}</p>
                        <p><strong>Low:</strong> ₹{stock_data['Low'].iloc[-1]:.2f}</p>
                        <p><strong>Volume:</strong> {stock_data['Volume'].iloc[-1]:,}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h3 class="gradient-text">Change</h3>
                        <div class="metric-value {change_class}"><span class="emoji-normal">{change_icon}</span> ₹{price_change:.2f}</div>
                        <div class="metric-label {change_class}">({price_change_pct:+.2f}%)</div>
                    </div>
                    <div class="flip-card-back">
                        <h4><span class="gradient-text">Change Analysis</span></h4>
                        <p><strong>Previous Close:</strong> ₹{prev_price:.2f}</p>
                        <p><strong>Change:</strong> ₹{price_change:.2f}</p>
                        <p><strong>% Change:</strong> {price_change_pct:+.2f}%</p>
                        <p><strong>Trend:</strong> {'Bullish' if price_change > 0 else 'Bearish' if price_change < 0 else 'Neutral'}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            volume = stock_data['Volume'].iloc[-1]
            avg_volume = stock_data['Volume'].mean()
            st.markdown(f"""
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h3 class="gradient-text">Volume</h3>
                        <div class="metric-value">{volume:,.0f}</div>
                        <div class="metric-label gradient-label">Shares Traded</div>
                    </div>
                    <div class="flip-card-back">
                        <h4><span class="gradient-text">Volume Analysis</span></h4>
                        <p><strong>Current:</strong> {volume:,.0f}</p>
                        <p><strong>Average:</strong> {avg_volume:,.0f}</p>
                        <p><strong>Ratio:</strong> {volume/avg_volume:.2f}x</p>
                        <p><strong>Activity:</strong> {'High' if volume > avg_volume * 1.5 else 'Normal' if volume > avg_volume * 0.5 else 'Low'}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            market_cap = f"₹{current_price * 1000000:.0f}M"  # Simplified calculation
            st.markdown(f"""
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <h3 class="gradient-text">Market Cap</h3>
                        <div class="metric-value">{market_cap}</div>
                        <div class="metric-label gradient-label">Approximate</div>
                    </div>
                    <div class="flip-card-back">
                        <h4><span class="gradient-text">Market Stats</span></h4>
                        <p><strong>52W High:</strong> ₹{stock_data['High'].max():.2f}</p>
                        <p><strong>52W Low:</strong> ₹{stock_data['Low'].min():.2f}</p>
                        <p><strong>Range:</strong> {((stock_data['High'].max() - stock_data['Low'].min()) / stock_data['Low'].min() * 100):.1f}%</p>
                        <p><strong>Position:</strong> {((current_price - stock_data['Low'].min()) / (stock_data['High'].max() - stock_data['Low'].min()) * 100):.1f}% of range</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    def create_price_chart(self, stock_data, stock_name):
        """Create an interactive price chart with candlesticks"""
        fig = go.Figure()
        
        # Add candlestick chart
        fig.add_trace(go.Candlestick(
            x=stock_data.index,
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close'],
            name=stock_name,
            increasing_line_color='#00ff88',
            decreasing_line_color='#ff4757'
        ))
        
        # Add moving averages
        stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()
        stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
        
        fig.add_trace(go.Scatter(
            x=stock_data.index,
            y=stock_data['MA20'],
            mode='lines',
            name='MA20',
            line=dict(color='#ffa502', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=stock_data.index,
            y=stock_data['MA50'],
            mode='lines',
            name='MA50',
            line=dict(color='#3742fa', width=2)
        ))
        
        # Update layout with darker text for better visibility
        fig.update_layout(
            title=dict(
                text=f"📈 {stock_name} - Price Chart",
                font=dict(color='#2c3e50', size=20, family="Arial Black")
            ),
            xaxis=dict(
                title=dict(text="Date", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            yaxis=dict(
                title=dict(text="Price (₹)", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            template="plotly_white",
            showlegend=True,
            height=500,
            paper_bgcolor='rgba(255,255,255,0.9)',
            plot_bgcolor='rgba(255,255,255,0.8)',
            legend=dict(
                font=dict(color='#2c3e50', size=12, family="Arial"),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#2c3e50',
                borderwidth=1
            )
        )
        
        return fig
    
    def create_volume_chart(self, stock_data, stock_name):
        """Create volume chart"""
        fig = go.Figure()
        
        # Color volume bars based on price change
        colors = ['#00ff88' if stock_data['Close'].iloc[i] >= stock_data['Open'].iloc[i] 
                 else '#ff4757' for i in range(len(stock_data))]
        
        fig.add_trace(go.Bar(
            x=stock_data.index,
            y=stock_data['Volume'],
            name='Volume',
            marker_color=colors,
            opacity=0.7
        ))
        
        fig.update_layout(
            title=dict(
                text=f"📊 {stock_name} - Volume",
                font=dict(color='#2c3e50', size=20, family="Arial Black")
            ),
            xaxis=dict(
                title=dict(text="Date", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            yaxis=dict(
                title=dict(text="Volume", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            template="plotly_white",
            height=500,
            paper_bgcolor='rgba(255,255,255,0.9)',
            plot_bgcolor='rgba(255,255,255,0.8)',
            legend=dict(
                font=dict(color='#2c3e50', size=12, family="Arial"),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#2c3e50',
                borderwidth=1
            )
        )
        
        return fig
    
    def display_technical_indicators(self, stock_data):
        """Display technical indicators"""
        st.markdown('<h2><span class="emoji-normal">📊</span> <span class="gradient-title">Technical Indicators</span></h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # RSI Calculation
            delta = stock_data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            current_rsi = rsi.iloc[-1]
            
            rsi_color = "price-up" if current_rsi < 30 else "price-down" if current_rsi > 70 else "price-neutral"
            
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label gradient-label">RSI (14)</div>
                <div class="metric-value {rsi_color}">{current_rsi:.2f}</div>
                <div class="metric-label gradient-label">{'Oversold' if current_rsi < 30 else 'Overbought' if current_rsi > 70 else 'Neutral'}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Bollinger Bands
            sma = stock_data['Close'].rolling(window=20).mean()
            std = stock_data['Close'].rolling(window=20).std()
            upper_band = sma + (std * 2)
            lower_band = sma - (std * 2)
            
            current_price = stock_data['Close'].iloc[-1]
            current_upper = upper_band.iloc[-1]
            current_lower = lower_band.iloc[-1]
            
            bb_position = (current_price - current_lower) / (current_upper - current_lower) * 100
            bb_color = "price-down" if bb_position > 80 else "price-up" if bb_position < 20 else "price-neutral"
            
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label gradient-label">Bollinger Bands</div>
                <div class="metric-value {bb_color}">{bb_position:.1f}%</div>
                <div class="metric-label gradient-label">Position in Band</div>
            </div>
            """, unsafe_allow_html=True)
    
    def create_prediction_chart(self, historical_data, predictions, stock_name):
        """Create prediction chart combining historical and predicted data"""
        fig = go.Figure()
        
        # Historical data
        fig.add_trace(go.Scatter(
            x=historical_data.index,
            y=historical_data['Close'],
            mode='lines',
            name='Historical Price',
            line=dict(color='#74b9ff', width=2)
        ))
        
        # Predicted data
        fig.add_trace(go.Scatter(
            x=predictions.index,
            y=predictions['Predicted_Price'],
            mode='lines',
            name='Predicted Price',
            line=dict(color='#ff7675', width=2, dash='dash')
        ))
        
        # Confidence intervals
        if 'Upper_Bound' in predictions.columns and 'Lower_Bound' in predictions.columns:
            fig.add_trace(go.Scatter(
                x=predictions.index,
                y=predictions['Upper_Bound'],
                mode='lines',
                name='Upper Bound',
                line=dict(color='rgba(255, 118, 117, 0.3)', width=1),
                showlegend=False
            ))
            
            fig.add_trace(go.Scatter(
                x=predictions.index,
                y=predictions['Lower_Bound'],
                mode='lines',
                name='Lower Bound',
                line=dict(color='rgba(255, 118, 117, 0.3)', width=1),
                fill='tonexty',
                fillcolor='rgba(255, 118, 117, 0.2)',
                showlegend=False
            ))
        
        fig.update_layout(
            title=dict(
                text=f"🔮 {stock_name} - Price Prediction till 2030",
                font=dict(color='#2c3e50', size=20, family="Arial Black")
            ),
            xaxis=dict(
                title=dict(text="Date", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            yaxis=dict(
                title=dict(text="Price (₹)", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            template="plotly_white",
            height=600,
            paper_bgcolor='rgba(255,255,255,0.9)',
            plot_bgcolor='rgba(255,255,255,0.8)',
            legend=dict(
                font=dict(color='#2c3e50', size=12, family="Arial"),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#2c3e50',
                borderwidth=1
            )
        )
        
        return fig
    
    def display_prediction_summary(self, predictions):
        """Display prediction summary statistics"""
        current_price = predictions['Predicted_Price'].iloc[0]
        final_price = predictions['Predicted_Price'].iloc[-1]
        price_change = final_price - current_price
        price_change_pct = (price_change / current_price) * 100
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            change_class = "price-up" if price_change > 0 else "price-down"
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label gradient-label">Predicted Change (5 Years)</div>
                <div class="metric-value {change_class}">₹{price_change:.2f}</div>
                <div class="metric-label {change_class}">({price_change_pct:+.1f}%)</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            annual_return = (price_change_pct / 5)
            return_class = "price-up" if annual_return > 0 else "price-down"
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label gradient-label">Expected Annual Return</div>
                <div class="metric-value {return_class}">{annual_return:.1f}%</div>
                <div class="metric-label gradient-label">Average per year</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            max_price = predictions['Predicted_Price'].max()
            min_price = predictions['Predicted_Price'].min()
            volatility = ((max_price - min_price) / current_price) * 100
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label gradient-label">Predicted Volatility</div>
                <div class="metric-value">{volatility:.1f}%</div>
                <div class="metric-label gradient-label">Price Range</div>
            </div>
            """, unsafe_allow_html=True)
    
    def display_educational_disclaimer(self):
        """Display educational disclaimer at the bottom of the page"""
        st.markdown("---")
        st.markdown("""
        <div style="
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(20px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 20px;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        ">
            <h4><span class="emoji-normal">📚</span> <span class="gradient-text">Educational Purpose Disclaimer</span></h4>
            <p style="margin: 5px 0; font-size: 14px; opacity: 0.9;" class="gradient-label">
                <strong>This demonstration is for educational purposes only.</strong><br>
                Built for project demonstration and learning purposes.<br>
                Not intended for actual investment decisions. Please consult financial advisors for investment advice.
            </p>
            <p style="margin: 5px 0; font-size: 12px; opacity: 0.7;" class="gradient-label">
                🇮🇳 Made with ❤️ for Indian Stock Market Learning
            </p>
        </div>
        """, unsafe_allow_html=True)
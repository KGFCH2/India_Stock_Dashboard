import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.stock_data import StockDataFetcher
from components.ui_components import UIComponents

def display_educational_disclaimer():
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
        <h4 style="color: #FF9933; margin-bottom: 10px;">📚 Educational Purpose Disclaimer</h4>
        <p style="margin: 5px 0; font-size: 14px; opacity: 0.9;">
            <strong>This demonstration is for educational purposes only.</strong><br>
            Built for project demonstration and learning purposes.<br>
            Not intended for actual investment decisions. Please consult financial advisors for investment advice.
        </p>
        <p style="margin: 5px 0; font-size: 12px; opacity: 0.7;">
            🇮🇳 Made with ❤️ for Indian Stock Market Learning
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_market_overview():
    """Display market overview page"""
    st.markdown("# 🏦 Market Overview")
    
    fetcher = StockDataFetcher()
    ui = UIComponents()
    
    # Market indices
    st.markdown("## 📊 Indian Market Indices")
    indices_data = fetcher.get_indian_market_indices()
    
    if indices_data:
        cols = st.columns(len(indices_data))
        
        for i, (name, data) in enumerate(indices_data.items()):
            with cols[i]:
                change_class = "price-up" if data['change'] > 0 else "price-down"
                change_icon = "📈" if data['change'] > 0 else "📉"
                
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{name}</div>
                    <div class="metric-value">{data['price']:.2f}</div>
                    <div class="metric-label {change_class}">
                        {change_icon} {data['change']:+.2f} ({data['change_pct']:+.2f}%)
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Top gainers and losers
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## 🚀 Top Gainers")
        gainers, losers = fetcher.get_top_gainers_losers()
        
        for stock in gainers:
            st.markdown(f"""
            <div class="glass-card">
                <strong>{stock['name']}</strong><br>
                ₹{stock['current_price']:.2f} 
                <span class="price-up">+{stock['change_pct']:.2f}%</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("## 📉 Top Losers")
        
        for stock in losers:
            st.markdown(f"""
            <div class="glass-card">
                <strong>{stock['name']}</strong><br>
                ₹{stock['current_price']:.2f} 
                <span class="price-down">{stock['change_pct']:.2f}%</span>
            </div>
            """, unsafe_allow_html=True)
    
    # Sector performance
    st.markdown("## 🏭 Sector Performance")
    sector_data = fetcher.get_sector_performance()
    
    if sector_data:
        sectors = list(sector_data.keys())
        performance = list(sector_data.values())
        
        fig = go.Figure(data=[
            go.Bar(
                x=sectors,
                y=performance,
                marker_color=['#00ff88' if p > 0 else '#ff4757' for p in performance],
                text=[f"{p:+.2f}%" for p in performance],
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            title=dict(
                text="Sector Performance Today",
                font=dict(color='#2c3e50', size=20, family="Arial Black")
            ),
            xaxis=dict(
                title=dict(text="Sectors", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            yaxis=dict(
                title=dict(text="Change (%)", font=dict(color='#2c3e50', size=14, family="Arial Black")),
                tickfont=dict(color='#2c3e50', size=12, family="Arial"),
                gridcolor='rgba(44, 62, 80, 0.3)'
            ),
            template="plotly_white",
            paper_bgcolor='rgba(255,255,255,0.9)',
            plot_bgcolor='rgba(255,255,255,0.8)',
            legend=dict(
                font=dict(color='#2c3e50', size=12, family="Arial"),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#2c3e50',
                borderwidth=1
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)

def show_portfolio():
    """Display portfolio tracking page"""
    st.markdown("# 💼 Portfolio Tracker")
    
    # Portfolio management would be implemented here
    st.info("Portfolio tracking feature - Coming Soon!")
    
    # Placeholder for portfolio features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## Add to Portfolio")
        with st.form("add_stock"):
            stock_symbol = st.text_input("Stock Symbol (e.g., RELIANCE.NS)")
            quantity = st.number_input("Quantity", min_value=1, value=1)
            buy_price = st.number_input("Buy Price", min_value=0.01, value=100.0)
            
            if st.form_submit_button("Add Stock"):
                st.success(f"Added {quantity} shares of {stock_symbol} at ₹{buy_price}")
    
    with col2:
        st.markdown("## Portfolio Summary")
        st.markdown("""
        <div class="glass-card">
            <h4>Total Portfolio Value</h4>
            <div class="metric-value">₹1,25,000</div>
            <div class="price-up">+₹5,000 (+4.17%)</div>
        </div>
        """, unsafe_allow_html=True)
def show_news():
    """Display market news page"""
    st.markdown("# 📰 Market News")
    
    fetcher = StockDataFetcher()
    news_data = fetcher.get_market_news()
    
    for news in news_data:
        st.markdown(f"""
        <div class="glass-card">
            <h4>{news['title']}</h4>
            <p>{news['summary']}</p>
            <small style="color: #74b9ff;">{news['time']}</small>
        </div>
        """, unsafe_allow_html=True)
def show_analytics():
    """Display advanced analytics page"""
    st.markdown("# 📈 Advanced Analytics")
    
    st.markdown("## 🎯 Stock Screener")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        min_price = st.number_input("Min Price", value=0.0)
        max_price = st.number_input("Max Price", value=10000.0)
    
    with col2:
        min_volume = st.number_input("Min Volume", value=0)
        rsi_filter = st.selectbox("RSI Filter", ["All", "Oversold (<30)", "Overbought (>70)"])
    
    with col3:
        sector_filter = st.selectbox("Sector", ["All", "Banking", "IT", "Auto", "Pharma", "FMCG"])
    
    if st.button("🔍 Screen Stocks"):
        st.info("Stock screening results would appear here...")
    
    # Correlation analysis
    st.markdown("## 🔗 Correlation Analysis")
    st.info("Correlation matrix between different stocks and indices would be displayed here.")
    
    # Technical analysis
    st.markdown("## 📊 Technical Analysis Tools")
    st.info("Advanced technical analysis tools and custom indicators would be available here.")
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class PredictionModel:
    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.lstm_model = None
        self.rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.linear_model = LinearRegression()
        
    def prepare_data_for_lstm(self, data, time_steps=60):
        """Prepare data for LSTM model"""
        scaled_data = self.scaler.fit_transform(data[['Close']].values)
        
        X, y = [], []
        for i in range(time_steps, len(scaled_data)):
            X.append(scaled_data[i-time_steps:i, 0])
            y.append(scaled_data[i, 0])
        
        return np.array(X), np.array(y)
    
    def create_lstm_model(self, input_shape):
        """Create LSTM model architecture"""
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=input_shape),
            Dropout(0.2),
            LSTM(50, return_sequences=True),
            Dropout(0.2),
            LSTM(50),
            Dropout(0.2),
            Dense(25),
            Dense(1)
        ])
        
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
    
    def train_lstm_model(self, X, y):
        """Train LSTM model"""
        # Reshape for LSTM
        X = X.reshape((X.shape[0], X.shape[1], 1))
        
        # Create and train model
        self.lstm_model = self.create_lstm_model((X.shape[1], 1))
        
        # Train with reduced epochs for faster execution
        self.lstm_model.fit(X, y, batch_size=32, epochs=10, verbose=0)
        
        return self.lstm_model
    
    def prepare_features(self, data):
        """Prepare features for machine learning models"""
        features = pd.DataFrame()
        
        # Price features
        features['Close'] = data['Close']
        features['High'] = data['High']
        features['Low'] = data['Low']
        features['Open'] = data['Open']
        features['Volume'] = data['Volume']
        
        # Technical indicators
        features['SMA_5'] = data['Close'].rolling(window=5).mean()
        features['SMA_20'] = data['Close'].rolling(window=20).mean()
        features['SMA_50'] = data['Close'].rolling(window=50).mean()
        
        # RSI
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        features['RSI'] = 100 - (100 / (1 + rs))
        
        # Bollinger Bands
        sma_20 = features['SMA_20']
        std_20 = data['Close'].rolling(window=20).std()
        features['BB_upper'] = sma_20 + (std_20 * 2)
        features['BB_lower'] = sma_20 - (std_20 * 2)
        features['BB_width'] = features['BB_upper'] - features['BB_lower']
        features['BB_position'] = (data['Close'] - features['BB_lower']) / features['BB_width']
        
        # Volume features
        features['Volume_SMA'] = data['Volume'].rolling(window=20).mean()
        features['Volume_ratio'] = data['Volume'] / features['Volume_SMA']
        
        # Price change features
        features['Price_change'] = data['Close'].pct_change()
        features['Price_change_5d'] = data['Close'].pct_change(5)
        features['Price_change_20d'] = data['Close'].pct_change(20)
        
        # Volatility
        features['Volatility'] = data['Close'].rolling(window=20).std()
        
        # Date features
        features['DayOfWeek'] = data.index.dayofweek
        features['Month'] = data.index.month
        features['Quarter'] = data.index.quarter
        
        # Drop NaN values
        features = features.dropna()
        
        return features
    
    def predict_future_prices(self, historical_data, symbol, years_ahead=5):
        """Predict future stock prices using ensemble of models"""
        try:
            if len(historical_data) < 100:
                # Use simple trend analysis for short datasets
                return self.simple_trend_prediction(historical_data, years_ahead)
            
            # Prepare features
            features = self.prepare_features(historical_data)
            
            if len(features) < 50:
                return self.simple_trend_prediction(historical_data, years_ahead)
            
            # Use multiple models for prediction
            predictions = self.ensemble_prediction(features, years_ahead)
            
            return predictions
            
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            return self.simple_trend_prediction(historical_data, years_ahead)
    
    def simple_trend_prediction(self, data, years_ahead):
        """Simple trend-based prediction for fallback"""
        # Calculate trend using linear regression on recent data
        recent_data = data.tail(252)  # Last year of data
        
        # Create time index
        x = np.arange(len(recent_data)).reshape(-1, 1)
        y = recent_data['Close'].values
        
        # Fit linear model
        self.linear_model.fit(x, y)
        
        # Generate future dates
        last_date = data.index[-1]
        future_dates = pd.date_range(
            start=last_date + timedelta(days=1),
            periods=years_ahead * 252,  # 252 trading days per year
            freq='B'  # Business days
        )
        
        # Predict future values
        future_x = np.arange(len(recent_data), len(recent_data) + len(future_dates)).reshape(-1, 1)
        future_prices = self.linear_model.predict(future_x)
        
        # Add some realistic volatility
        volatility = data['Close'].pct_change().std() * np.sqrt(252)  # Annualized volatility
        random_factor = np.random.normal(1, volatility/4, len(future_prices))
        future_prices = future_prices * random_factor
        
        # Ensure prices don't go negative
        future_prices = np.maximum(future_prices, data['Close'].iloc[-1] * 0.1)
        
        # Create prediction dataframe
        predictions = pd.DataFrame({
            'Predicted_Price': future_prices,
            'Upper_Bound': future_prices * 1.2,
            'Lower_Bound': future_prices * 0.8
        }, index=future_dates)
        
        return predictions
    
    def ensemble_prediction(self, features, years_ahead):
        """Use ensemble of models for prediction"""
        # Prepare target variable (next day's closing price)
        target = features['Close'].shift(-1).dropna()
        features_aligned = features[:-1]  # Remove last row to align with target
        
        # Split data
        split_point = int(len(features_aligned) * 0.8)
        X_train = features_aligned[:split_point]
        y_train = target[:split_point]
        X_test = features_aligned[split_point:]
        
        # Select numeric features only
        numeric_features = X_train.select_dtypes(include=[np.number]).columns
        X_train_numeric = X_train[numeric_features].fillna(X_train[numeric_features].mean())
        X_test_numeric = X_test[numeric_features].fillna(X_train[numeric_features].mean())
        
        # Train Random Forest model
        self.rf_model.fit(X_train_numeric, y_train)
        
        # Generate future predictions
        last_features = X_test_numeric.iloc[-1:].copy()
        
        future_dates = pd.date_range(
            start=features.index[-1] + timedelta(days=1),
            periods=years_ahead * 252,
            freq='B'
        )
        
        predictions = []
        current_features = last_features.copy()
        
        for i in range(len(future_dates)):
            # Predict next price
            next_price = self.rf_model.predict(current_features)[0]
            predictions.append(next_price)
            
            # Update features for next prediction
            # This is a simplified approach - in practice, you'd update all relevant features
            current_features['Close'] = next_price
            
            # Add some trend and seasonality
            if i > 0:
                # Add slight upward trend (assuming long-term growth)
                trend_factor = 1 + (0.08 / 252)  # 8% annual growth rate
                next_price *= trend_factor
                
                # Add seasonal effects
                month = future_dates[i].month
                seasonal_factor = 1 + 0.02 * np.sin(2 * np.pi * month / 12)
                next_price *= seasonal_factor
            
            predictions[-1] = next_price
        
        # Calculate confidence intervals
        volatility = features['Close'].pct_change().std() * np.sqrt(252)
        
        predictions_array = np.array(predictions)
        upper_bound = predictions_array * (1 + volatility)
        lower_bound = predictions_array * (1 - volatility)
        
        # Create prediction dataframe
        prediction_df = pd.DataFrame({
            'Predicted_Price': predictions_array,
            'Upper_Bound': upper_bound,
            'Lower_Bound': lower_bound
        }, index=future_dates)
        
        return prediction_df
    
    def get_prediction_accuracy_metrics(self, actual, predicted):
        """Calculate prediction accuracy metrics"""
        mse = np.mean((actual - predicted) ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(actual - predicted))
        mape = np.mean(np.abs((actual - predicted) / actual)) * 100
        
        return {
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'MAPE': mape
        }
    
    def generate_prediction_insights(self, historical_data, predictions):
        """Generate insights from predictions"""
        current_price = historical_data['Close'].iloc[-1]
        final_predicted_price = predictions['Predicted_Price'].iloc[-1]
        
        # Calculate expected returns
        total_return = (final_predicted_price - current_price) / current_price * 100
        annual_return = (total_return / len(predictions)) * 252  # Annualized
        
        # Risk analysis
        predicted_volatility = predictions['Predicted_Price'].pct_change().std() * np.sqrt(252) * 100
        
        # Trend analysis
        trend_direction = "Upward" if final_predicted_price > current_price else "Downward"
        
        insights = {
            'current_price': current_price,
            'predicted_final_price': final_predicted_price,
            'total_expected_return': total_return,
            'annual_expected_return': annual_return,
            'predicted_volatility': predicted_volatility,
            'trend_direction': trend_direction,
            'confidence_level': 'Medium',  # This would be calculated based on model performance
            'risk_level': 'High' if predicted_volatility > 30 else 'Medium' if predicted_volatility > 15 else 'Low'
        }
        
        return insights
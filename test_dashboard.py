"""
Test script for Indian Stock Market Dashboard
"""

import sys
import os
import importlib.util

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    required_modules = [
        'streamlit',
        'pandas', 
        'plotly',
        'yfinance',
        'numpy',
        'sklearn',
        'tensorflow'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n❌ Missing modules: {', '.join(missing_modules)}")
        print("Please install missing modules using:")
        print("pip install -r requirements.txt")
        return False
    
    print("\n✅ All required modules are available!")
    return True

def test_file_structure():
    """Test if all required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'main.py',
        'requirements.txt',
        'components/auth.py',
        'components/ui_components.py',
        'utils/stock_data.py',
        'utils/prediction_model.py',
        'pages/dashboard_pages.py',
        '.streamlit/config.toml'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("\n✅ All required files are present!")
    return True

def test_stock_data():
    """Test stock data fetching functionality"""
    print("\nTesting stock data fetching...")
    
    try:
        from utils.stock_data import StockDataFetcher
        fetcher = StockDataFetcher()
        
        # Test with a popular Indian stock
        data = fetcher.get_stock_data("RELIANCE.NS", "5d")
        
        if data is not None and not data.empty:
            print("✅ Stock data fetching works!")
            print(f"   Sample data shape: {data.shape}")
            return True
        else:
            print("❌ Stock data fetching failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing stock data: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Running Indian Stock Market Dashboard Tests")
    print("=" * 50)
    
    tests = [
        test_file_structure,
        test_imports,
        test_stock_data
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Dashboard is ready to run.")
        print("\nTo start the dashboard, run:")
        print("python run_dashboard.py")
        print("or")
        print("streamlit run main.py")
    else:
        print("❌ Some tests failed. Please fix the issues before running the dashboard.")

if __name__ == "__main__":
    main()
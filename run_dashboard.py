#!/usr/bin/env python3
"""
Indian Stock Market Dashboard Startup Script
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements. Please install manually.")
        return False
    return True

def run_dashboard():
    """Run the Streamlit dashboard"""
    print("Starting Indian Stock Market Dashboard...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "main.py", "--server.port=8501"])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user.")
    except Exception as e:
        print(f"❌ Error running dashboard: {e}")

def main():
    """Main startup function"""
    print("🚀 Indian Stock Market Dashboard")
    print("=" * 40)
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Run dashboard
    run_dashboard()

if __name__ == "__main__":
    main()
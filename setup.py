#!/usr/bin/env python3
"""
Setup script for Playwright tests
Run this once to set up the environment
"""

import subprocess
import sys
import os

def setup_environment():
    """Set up the testing environment"""
    print("🔧 Setting up Playwright test environment...")
    
    # Install requirements
    print("📦 Installing Python packages...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    
    # Install Playwright browsers
    print("🌐 Installing Playwright browsers...")
    subprocess.run([sys.executable, '-m', 'playwright', 'install'], check=True)
    
    print("✅ Setup complete! You can now run tests.")
    print("\nTo run tests:")
    print("  python run_tests.py")
    print("  or")
    print("  python -m pytest tests/ -v")

if __name__ == "__main__":
    setup_environment()


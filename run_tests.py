#!/usr/bin/env python3
"""
Simple script to run Playwright tests
Usage: python run_tests.py
"""

import subprocess
import sys
import os

def run_tests():
    """Run the Playwright tests"""
    print("🚀 Starting Playwright tests...")
    print("=" * 50)
    
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        # Run pytest with verbose output for all tests in tests folder
        result = subprocess.run([
            sys.executable, '-m', 'pytest', 
            'tests/', 
            '-v', '--tb=short'
        ], check=False, capture_output=False)
        
        print("=" * 50)
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed!")
            
        return result.returncode
        
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)


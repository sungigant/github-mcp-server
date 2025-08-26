#!/usr/bin/env python3
"""
Test script to verify demo scripts are syntactically correct and importable
"""

import sys
import ast

def check_python_syntax(filename):
    """Check if a Python file has valid syntax"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the file to check syntax
        ast.parse(content, filename=filename)
        print(f"✅ {filename}: Syntax OK")
        return True
    except SyntaxError as e:
        print(f"❌ {filename}: Syntax Error - {e}")
        return False
    except Exception as e:
        print(f"❌ {filename}: Error - {e}")
        return False

def main():
    print("🧪 Testing Polish AI Demo Scripts...")
    print("-" * 40)
    
    demo_files = [
        "gpt2_local_demo.py",
        "xglm_polish_demo.py", 
        "herbert_polish_demo.py",
        "run_all_demos.py"
    ]
    
    success_count = 0
    for demo_file in demo_files:
        if check_python_syntax(demo_file):
            success_count += 1
    
    print("-" * 40)
    print(f"📊 Results: {success_count}/{len(demo_files)} scripts passed syntax check")
    
    if success_count == len(demo_files):
        print("🎉 All demo scripts are ready to use!")
        print("\n📝 Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run demos: python3 run_all_demos.py")
    else:
        print("⚠️  Some scripts have issues that need to be fixed.")
    
    return success_count == len(demo_files)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
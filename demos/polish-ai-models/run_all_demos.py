#!/usr/bin/env python3
"""
All-in-One Polish AI Models Demo Runner

This script allows you to test all available Polish AI models in one place.
You can choose which model to run or run all of them sequentially.
"""

import sys
import subprocess

def print_banner():
    print("=" * 60)
    print("🇵🇱 POLISH AI MODELS - LOCAL DEMO RUNNER 🇵🇱")
    print("=" * 60)
    print("Available Models:")
    print("1. GPT-2 Local Demo (Basic Polish support)")
    print("2. XGLM-564M Demo (Recommended - Excellent Polish)")
    print("3. HerBERT Demo (Polish BERT for understanding)")
    print("4. Run All Models")
    print("0. Exit")
    print("=" * 60)

def run_demo(script_name):
    """Run a specific demo script"""
    try:
        print(f"\n🚀 Running {script_name}...")
        print("-" * 40)
        result = subprocess.run([sys.executable, script_name], 
                               capture_output=False, text=True)
        print("-" * 40)
        print(f"✅ {script_name} completed with exit code: {result.returncode}")
        return result.returncode == 0
    except FileNotFoundError:
        print(f"❌ Error: {script_name} not found!")
        return False
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")
        return False

def main():
    while True:
        print_banner()
        
        try:
            choice = input("\nEnter your choice (0-4): ").strip()
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        
        if choice == "0":
            print("👋 Goodbye!")
            break
        elif choice == "1":
            run_demo("gpt2_local_demo.py")
        elif choice == "2":
            run_demo("xglm_polish_demo.py")
        elif choice == "3":
            run_demo("herbert_polish_demo.py")
        elif choice == "4":
            print("\n🚀 Running all models sequentially...")
            demos = [
                "gpt2_local_demo.py",
                "xglm_polish_demo.py", 
                "herbert_polish_demo.py"
            ]
            
            success_count = 0
            for demo in demos:
                if run_demo(demo):
                    success_count += 1
                print("\n" + "="*20 + " NEXT MODEL " + "="*20 + "\n")
            
            print(f"📊 Summary: {success_count}/{len(demos)} models ran successfully")
        else:
            print("❌ Invalid choice. Please enter 0-4.")
        
        if choice != "0":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
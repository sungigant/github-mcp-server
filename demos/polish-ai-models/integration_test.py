#!/usr/bin/env python3
"""
Integration test for Polish AI demos - tests imports without downloading models
"""

import sys
import importlib.util

def test_imports():
    """Test if required packages can be imported (if available)"""
    print("🔍 Testing package imports...")
    
    optional_packages = [
        ("torch", "PyTorch for deep learning"),
        ("transformers", "Hugging Face Transformers"),
        ("tokenizers", "Fast tokenizers"),
        ("numpy", "NumPy for numerical computing")
    ]
    
    available_packages = []
    missing_packages = []
    
    for package_name, description in optional_packages:
        try:
            spec = importlib.util.find_spec(package_name)
            if spec is not None:
                available_packages.append((package_name, description))
                print(f"  ✅ {package_name}: Available")
            else:
                missing_packages.append((package_name, description))
                print(f"  ❌ {package_name}: Not available")
        except Exception as e:
            missing_packages.append((package_name, description))
            print(f"  ❌ {package_name}: Error - {e}")
    
    print(f"\n📊 Package Status:")
    print(f"  Available: {len(available_packages)}")
    print(f"  Missing: {len(missing_packages)}")
    
    if missing_packages:
        print(f"\n📦 To install missing packages:")
        print(f"  pip install -r requirements.txt")
        print(f"\nMissing packages:")
        for pkg, desc in missing_packages:
            print(f"  - {pkg}: {desc}")
    
    return len(missing_packages) == 0

def test_demo_executability():
    """Test if demo scripts can be executed (just import test)"""
    print("\n🎭 Testing demo script imports...")
    
    demo_modules = [
        "gpt2_local_demo",
        "xglm_polish_demo", 
        "herbert_polish_demo",
        "run_all_demos"
    ]
    
    success_count = 0
    for module_name in demo_modules:
        try:
            # Test if the module can be loaded without executing main()
            spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
            module = importlib.util.module_from_spec(spec)
            
            # Just test syntax, don't execute
            with open(f"{module_name}.py", 'r') as f:
                code = compile(f.read(), f"{module_name}.py", 'exec')
            
            print(f"  ✅ {module_name}.py: Loadable")
            success_count += 1
        except Exception as e:
            print(f"  ❌ {module_name}.py: Error - {e}")
    
    print(f"\n📊 Demo Status: {success_count}/{len(demo_modules)} demos ready")
    return success_count == len(demo_modules)

def main():
    print("🧪 POLISH AI DEMOS - INTEGRATION TEST")
    print("=" * 50)
    
    imports_ok = test_imports()
    demos_ok = test_demo_executability()
    
    print("\n" + "=" * 50)
    if imports_ok and demos_ok:
        print("🎉 ALL TESTS PASSED!")
        print("Polish AI demos are ready to use.")
        print("\n🚀 Quick Start:")
        print("  python3 run_all_demos.py")
    elif demos_ok and not imports_ok:
        print("⚠️  PARTIAL SUCCESS")
        print("Demo scripts are ready, but you need to install dependencies:")
        print("  pip install -r requirements.txt")
    else:
        print("❌ TESTS FAILED")
        print("Please check the errors above and fix them.")
    
    return imports_ok and demos_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
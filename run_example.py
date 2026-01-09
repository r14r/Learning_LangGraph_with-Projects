#!/usr/bin/env python3
"""
Helper script to run and test LangGraph examples
"""
import sys
import subprocess
import argparse
from pathlib import Path


def list_examples():
    """List all available examples."""
    base_path = Path(__file__).parent
    
    print("\n📚 Available Examples:\n")
    
    for level in ["Beginner", "Advanced", "Expert"]:
        level_path = base_path / level
        if level_path.exists():
            print(f"\n{level}:")
            examples = sorted(level_path.glob("Example_*"))
            for i, example in enumerate(examples, 1):
                print(f"  {i:2d}. {example.name}")


def run_example(level, number):
    """Run a specific example."""
    base_path = Path(__file__).parent
    
    # Find the example directory
    level_path = base_path / level
    matches = list(level_path.glob(f"Example_{number:02d}_*"))
    
    if not matches:
        print(f"❌ Example not found: {level}/Example_{number:02d}")
        return False
    
    example_path = matches[0]
    app_path = example_path / "app.py"
    
    if not app_path.exists():
        print(f"❌ app.py not found in {example_path}")
        return False
    
    print(f"🚀 Running {example_path.name}...")
    print(f"📁 Path: {example_path}")
    print(f"\n🌐 Opening Streamlit app at http://localhost:8501\n")
    
    try:
        subprocess.run(["streamlit", "run", str(app_path)])
        return True
    except KeyboardInterrupt:
        print("\n\n✋ Stopped by user")
        return True
    except Exception as e:
        print(f"❌ Error running example: {e}")
        return False


def test_example(level, number):
    """Test a specific example."""
    base_path = Path(__file__).parent
    
    # Find the example directory
    level_path = base_path / level
    matches = list(level_path.glob(f"Example_{number:02d}_*"))
    
    if not matches:
        print(f"❌ Example not found: {level}/Example_{number:02d}")
        return False
    
    example_path = matches[0]
    test_path = example_path / "test.py"
    
    if not test_path.exists():
        print(f"❌ test.py not found in {example_path}")
        return False
    
    print(f"🧪 Testing {example_path.name}...")
    
    try:
        result = subprocess.run(
            ["pytest", str(test_path), "-v"],
            cwd=str(example_path)
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error testing example: {e}")
        return False


def test_all(level=None):
    """Test all examples or all in a specific level."""
    base_path = Path(__file__).parent
    
    if level:
        pattern = f"{level}/*/test.py"
        print(f"🧪 Testing all {level} examples...\n")
    else:
        pattern = "*/*/test.py"
        print("🧪 Testing all examples...\n")
    
    try:
        result = subprocess.run(["pytest", pattern, "-v"])
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error testing: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Helper script for LangGraph Streamlit examples"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # List command
    subparsers.add_parser("list", help="List all examples")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run an example")
    run_parser.add_argument("level", choices=["Beginner", "Advanced", "Expert"],
                           help="Example level")
    run_parser.add_argument("number", type=int, help="Example number (1-10)")
    
    # Test command
    test_parser = subparsers.add_parser("test", help="Test an example")
    test_parser.add_argument("level", choices=["Beginner", "Advanced", "Expert"],
                            help="Example level")
    test_parser.add_argument("number", type=int, help="Example number (1-10)")
    
    # Test-all command
    test_all_parser = subparsers.add_parser("test-all", help="Test all examples")
    test_all_parser.add_argument("--level", choices=["Beginner", "Advanced", "Expert"],
                                help="Test only this level")
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_examples()
    elif args.command == "run":
        success = run_example(args.level, args.number)
        sys.exit(0 if success else 1)
    elif args.command == "test":
        success = test_example(args.level, args.number)
        sys.exit(0 if success else 1)
    elif args.command == "test-all":
        success = test_all(args.level)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

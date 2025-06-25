#!/usr/bin/env python3
"""
🚀 Cursor Unlimited Tool Calls (CUTC) - Ultra-Optimized Installer
One-click installation script that contains everything needed and self-destructs after setup.

Usage: python install.py [--keep-installer]
"""

import os
import sys
import shutil
from pathlib import Path
import argparse

# Embedded file contents
USERINPUT_CONTENT = '''user_input = input("prompt: ")'''

RULES_CONTENT = '''---
description: Cursor Unlimited Tool Calls (CUTC) - Maximize your tool calls
globs: 
alwaysApply: true
---

### ✅ Task: Interactive Task Loop with User Feedback

1. **Check if `userinput.py` exists** in the root directory.

   * If it doesn't exist, create it with the following content:

     ```python
     # userinput.py
     user_input = input("prompt: ")
     ```

2. **Main Workflow**:

   * Perform your assigned tasks.

   * Run:

     ```bash
     python userinput.py
     ```
   * The terminal should be opened in the chat window itself.

   * Read the user's input.

   * Based on the input, perform the next set of tasks.

   * Repeat the process.

3. **Exit Condition**:

   * If the user enters `"stop"` when prompted, exit the loop and terminate the process.'''

def print_header():
    """Print installation header"""
    print("🚀 CUTC Ultra-Optimized Installer")
    print("=" * 50)
    print("Installing Cursor Unlimited Tool Calls...")
    print()

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6+ required. Current version:", sys.version)
        return False
    
    # Check if we're in a valid directory
    if not os.access(".", os.W_OK):
        print("❌ No write permissions in current directory")
        return False
    
    print("✅ Prerequisites check passed")
    return True

def create_cursor_structure():
    """Create .cursor/rules/ structure"""
    print("📁 Creating Cursor structure...")
    
    cursor_dir = Path(".cursor")
    rules_dir = cursor_dir / "rules"
    
    try:
        rules_dir.mkdir(parents=True, exist_ok=True)
        print("✅ .cursor/rules/ structure created")
        return rules_dir
    except Exception as e:
        print(f"❌ Failed to create directory structure: {e}")
        return None

def install_files(rules_dir):
    """Install all necessary files"""
    print("📝 Installing CUTC files...")
    
    try:
        # Install userinput.py at root
        with open("userinput.py", "w", encoding="utf-8") as f:
            f.write(USERINPUT_CONTENT)
        print("✅ userinput.py installed at project root")
        
        # Install rules file
        rules_file = rules_dir / "cutc_rules.mdc"
        with open(rules_file, "w", encoding="utf-8") as f:
            f.write(RULES_CONTENT)
        print(f"✅ CUTC rules installed: {rules_file}")
        
        return True
    except Exception as e:
        print(f"❌ Failed to install files: {e}")
        return False

def print_success_message():
    """Print success message and next steps"""
    print()
    print("🎉 CUTC Installation Completed Successfully!")
    print("=" * 50)
    print()
    print("📋 Next Steps:")
    print("1. 🔄 Restart Cursor IDE")
    print("2. ⚙️  Verify CUTC rules are active in settings")
    print("3. 🤖 Switch to Agent Mode")
    print("4. 🚀 Start coding with unlimited tool calls!")
    print()
    print("💡 Usage Tips:")
    print("• When AI finishes a task, it will prompt: 'prompt:'")
    print("• Type your next instruction to continue")
    print("• Type 'stop' to end the loop")
    print()
    print("🆘 Need help? Visit: https://github.com/Thorrdu/CUTC")
    print("☕ Support: https://ko-fi.com/thorrdu")

def self_destruct(keep_installer=False):
    """Self-destruct this installer after successful installation"""
    if keep_installer:
        print("🔧 Installer kept for debugging (--keep-installer flag used)")
        return
    
    try:
        installer_path = Path(__file__)
        if installer_path.exists():
            installer_path.unlink()
            print("🗑️  Installer self-destructed successfully")
            print("   (Keeping your project clean!)")
    except Exception as e:
        print(f"⚠️  Could not self-destruct installer: {e}")
        print("   You can manually delete 'install.py' if desired")

def handle_installation_error():
    """Handle installation errors gracefully"""
    print()
    print("❌ Installation Failed!")
    print("=" * 30)
    print()
    print("🛠️  Troubleshooting:")
    print("• Ensure you have write permissions in this directory")
    print("• Make sure Cursor IDE is closed during installation")
    print("• Try running as administrator (Windows) or with sudo (Linux/Mac)")
    print()
    print("🆘 Still having issues?")
    print("• Visit: https://github.com/Thorrdu/CUTC/issues")
    print("• Or contact: https://ko-fi.com/thorrdu")

def main():
    """Main installation function"""
    parser = argparse.ArgumentParser(description="CUTC Ultra-Optimized Installer")
    parser.add_argument("--keep-installer", action="store_true", 
                       help="Keep the installer file after installation")
    args = parser.parse_args()
    
    print_header()
    
    # Check prerequisites
    if not check_prerequisites():
        handle_installation_error()
        return 1
    
    # Create directory structure
    rules_dir = create_cursor_structure()
    if not rules_dir:
        handle_installation_error()
        return 1
    
    # Install files
    if not install_files(rules_dir):
        handle_installation_error()
        return 1
    
    # Success!
    print_success_message()
    
    # Self-destruct (unless debugging)
    self_destruct(args.keep_installer)
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation cancelled by user")
        print("No files were modified.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        handle_installation_error()
        sys.exit(1) 
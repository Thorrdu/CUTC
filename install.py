#!/usr/bin/env python3
"""
Cursor Unlimited Tool Calls (CUTC) - Automatic Installation
Installation script to configure CUTC in your existing project
"""

import os
import shutil
from pathlib import Path

def create_cursor_structure():
    """Creates the .cursor/rules/ structure if it doesn't exist"""
    cursor_dir = Path(".cursor")
    rules_dir = cursor_dir / "rules"
    
    # Create directories
    rules_dir.mkdir(parents=True, exist_ok=True)
    print("✅ .cursor/rules/ structure created")
    
    return rules_dir

def install_userinput():
    """Installs the userinput.py file at the project root"""
    userinput_content = 'user_input = input("prompt: ")\n'
    
    with open("userinput.py", "w", encoding="utf-8") as f:
        f.write(userinput_content)
    
    print("✅ userinput.py installed at root")

def install_rules(rules_dir):
    """Installs the CUTC rules file"""
    rules_content = """---
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

   * If the user enters `"stop"` when prompted, exit the loop and terminate the process.
"""
    
    rules_file = rules_dir / "cutc_rules.mdc"
    with open(rules_file, "w", encoding="utf-8") as f:
        f.write(rules_content)
    
    print(f"✅ CUTC rules installed in {rules_file}")

def main():
    """Main CUTC installation"""
    print("🚀 Installing Cursor Unlimited Tool Calls (CUTC)")
    print("-" * 50)
    
    try:
        # Check if we're in a project
        if not os.path.exists("."):
            print("❌ Error: Run this script at the root of your project")
            return
        
        # Create .cursor structure
        rules_dir = create_cursor_structure()
        
        # Install userinput.py
        install_userinput()
        
        # Install rules
        install_rules(rules_dir)
        
        print("-" * 50)
        print("🎉 Installation completed successfully!")
        print("\n📋 Next steps:")
        print("1. Restart Cursor IDE")
        print("2. Verify that CUTC rules are active in settings")
        print("3. Start using Agent mode with your tasks")
        print("\n💡 Type 'stop' in the prompt to end the loop")
        
    except Exception as e:
        print(f"❌ Error during installation: {e}")
        print("Contact us at https://ko-fi.com/thorrdu for help")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
🚀 Cursor Unlimited Tool Calls (CUTC) - Ultra-Optimized Installer
One-click installation script that contains everything needed and self-destructs after setup.
Supports both Cursor IDE and Windsurf IDE.

Usage: 
  python install.py                    # Auto-detect IDE or prompt for selection
  python install.py --ide cursor      # Install for Cursor IDE
  python install.py --ide windsurf    # Install for Windsurf IDE
  python install.py --keep-installer  # Keep installer for debugging
"""

import os
import sys
import shutil
from pathlib import Path
import argparse

def load_source_file(filename):
    """Load content from src/ directory"""
    src_path = Path("src") / filename
    if not src_path.exists():
        raise FileNotFoundError(f"Source file not found: {src_path}")
    
    with open(src_path, "r", encoding="utf-8") as f:
        return f.read()



def print_header():
    """Print installation header"""
    print("🚀 CUTC Ultra-Optimized Installer")
    print("=" * 50)
    print("Installing Cursor Unlimited Tool Calls...")
    print("Supports: Cursor IDE & Windsurf IDE")
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
    
    # Check if src/ directory exists
    src_dir = Path("src")
    if not src_dir.exists():
        print("❌ Source directory 'src/' not found")
        print("   Make sure you have the complete CUTC package with src/ folder")
        return False
    
    # Check if required source files exist
    required_files = ["userinput.py", "cutc_rules.mdc"]
    for file in required_files:
        if not (src_dir / file).exists():
            print(f"❌ Required source file not found: src/{file}")
            return False
    
    print("✅ Prerequisites check passed")
    return True

def detect_ide():
    """Auto-detect which IDE is being used"""
    print("🔍 Auto-detecting IDE...")
    
    # Check for existing IDE structures
    cursor_exists = Path(".cursor").exists()
    windsurf_exists = Path(".windsurf").exists()
    
    if cursor_exists and windsurf_exists:
        print("⚠️  Both Cursor and Windsurf structures detected")
        return None
    elif cursor_exists:
        print("✅ Cursor IDE structure detected")
        return "cursor"
    elif windsurf_exists:
        print("✅ Windsurf IDE structure detected")
        return "windsurf"
    else:
        print("ℹ️  No IDE structure detected")
        return None

def prompt_ide_selection():
    """Prompt user to select IDE if auto-detection fails"""
    print("🤔 Which IDE would you like to install CUTC for?")
    print("1. Cursor IDE")
    print("2. Windsurf IDE")
    print("3. Both (install for both IDEs)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1/2/3): ").strip()
            if choice == "1":
                return "cursor"
            elif choice == "2":
                return "windsurf"
            elif choice == "3":
                return "both"
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Installation cancelled by user")
            sys.exit(1)

def create_ide_structure(ide):
    """Create IDE-specific structure"""
    print(f"📁 Creating {ide.upper()} structure...")
    
    if ide == "cursor":
        rules_dir = Path(".cursor") / "rules"
        rules_dir.mkdir(parents=True, exist_ok=True)
        print("✅ .cursor/rules/ structure created")
        return rules_dir
    elif ide == "windsurf":
        rules_dir = Path(".windsurf") / "rules"
        rules_dir.mkdir(parents=True, exist_ok=True)
        print("✅ .windsurf/rules/ structure created")
        return rules_dir
    else:
        raise ValueError(f"Unsupported IDE: {ide}")

def install_files(ide, rules_dir=None):
    """Install all necessary files for the specified IDE"""
    print(f"📝 Installing CUTC files for {ide.upper()}...")
    
    try:
        # Load userinput.py content from src/
        userinput_content = load_source_file("userinput.py")
        
        # Install userinput.py at root (same for both IDEs)
        with open("userinput.py", "w", encoding="utf-8") as f:
            f.write(userinput_content)
        print("✅ userinput.py installed at project root")
        
        # Load base rules content from src/
        base_rules_content = load_source_file("cutc_rules.mdc")
        
        # Install IDE-specific rules file with appropriate extension
        if ide == "cursor":
            rules_file = rules_dir / "cutc_rules.mdc"
            with open(rules_file, "w", encoding="utf-8") as f:
                f.write(base_rules_content)
            print(f"✅ CUTC rules installed: {rules_file}")
        elif ide == "windsurf":
            rules_file = rules_dir / "cutc_rules.md"
            with open(rules_file, "w", encoding="utf-8") as f:
                f.write(base_rules_content)
            print(f"✅ CUTC rules installed: {rules_file}")
        
        return True
    except Exception as e:
        print(f"❌ Failed to install files: {e}")
        return False

def install_for_ide(ide):
    """Install CUTC for a specific IDE"""
    rules_dir = create_ide_structure(ide)
    if not rules_dir:
        return False
    
    return install_files(ide, rules_dir)

def print_success_message(ide):
    """Print success message and next steps"""
    print()
    print("🎉 CUTC Installation Completed Successfully!")
    print("=" * 50)
    print()
    
    if ide == "cursor":
        print("📋 Next Steps for Cursor IDE:")
        print("1. 🔄 Restart Cursor IDE")
        print("2. ⚙️  Configure CUTC rules (see README for options)")
        print("3. 🤖 Switch to Agent Mode")
        print("4. 🚀 Start coding with unlimited tool calls!")
    elif ide == "windsurf":
        print("📋 Next Steps for Windsurf IDE:")
        print("1. 🔄 Restart Windsurf IDE")
        print("2. ⚙️  Configure CUTC rules (see README for options)")
        print("3. 🤖 Switch to Cascade Mode")
        print("4. 🚀 Start coding with unlimited tool calls!")
    elif ide == "both":
        print("📋 Next Steps:")
        print("1. 🔄 Restart your IDE(s)")
        print("2. ⚙️  Configure CUTC rules (see README for options)")
        print("3. 🤖 Switch to Agent/Cascade Mode")
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
    print("• Make sure your IDE is closed during installation")
    print("• Try running as administrator (Windows) or with sudo (Linux/Mac)")
    print()
    print("🆘 Still having issues?")
    print("• Visit: https://github.com/Thorrdu/CUTC/issues")
    print("• Or contact: https://ko-fi.com/thorrdu")

def main():
    """Main installation function"""
    parser = argparse.ArgumentParser(description="CUTC Ultra-Optimized Installer")
    parser.add_argument("--ide", choices=["cursor", "windsurf", "both"], 
                       help="Target IDE (cursor, windsurf, or both)")
    parser.add_argument("--keep-installer", action="store_true", 
                       help="Keep the installer file after installation")
    args = parser.parse_args()
    
    print_header()
    
    # Check prerequisites
    if not check_prerequisites():
        handle_installation_error()
        return 1
    
    # Determine target IDE
    if args.ide:
        target_ide = args.ide
        print(f"🎯 Target IDE specified: {target_ide.upper()}")
    else:
        detected_ide = detect_ide()
        if detected_ide:
            target_ide = detected_ide
        else:
            target_ide = prompt_ide_selection()
    
    # Install for target IDE(s)
    success = True
    
    if target_ide == "both":
        print("\n📦 Installing for both Cursor and Windsurf...")
        cursor_success = install_for_ide("cursor")
        windsurf_success = install_for_ide("windsurf")
        success = cursor_success and windsurf_success
    else:
        success = install_for_ide(target_ide)
    
    if not success:
        handle_installation_error()
        return 1
    
    # Success!
    print_success_message(target_ide)
    
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
# 🚀 Cursor Unlimited Tool Calls (CUTC)

**CUTC** is an ultra-minimalist tool designed for **Cursor IDE**, **Windsurf IDE**, or any other agent-based coding assistant that supports tool calls. It helps you get the **maximum value from your monthly tool call allowance** by running your tasks in a loop with user input—without restarting the chat every time.

> **Important Note:** This only works with **Agent Mode** (Cursor) or **Cascade Mode** (Windsurf)

---

## 🔄 Fork and Improvements

This project is an improved fork of the original [10x-Tool-Calls](https://github.com/perrypixel/10x-Tool-Calls) by [@perrypixel](https://github.com/perrypixel). 

**Huge thanks to perrypixel for the pioneering work!** 🙏

### 🎯 What we've improved:

- **Ultra-minimalist design**: Only 2 files in the entire project
- **Dual IDE support**: Works with both Cursor and Windsurf
- **Smart auto-detection**: Automatically detects your IDE setup
- **Self-destructing installer**: Keeps your project clean after installation
- **Zero configuration**: One command does everything
- **Enhanced error handling**: Smart troubleshooting and recovery
- **Cross-platform support**: Works on Windows, Mac, and Linux

### ✨ New Features: Image and File Context

CUTC now supports providing images and files as direct context in your prompts.

- **🖼️ Image Context**: Provide a path to an image (`.png`, `.jpg`, etc.), and the agent will "see" it.
- **📄 File Context**: Provide a path to a text file, and the agent will read its content.

---

## ✅ What CUTC Does

- After the AI completes a task, it runs a small Python script that asks:

```
prompt (or file path): 
```

- You can type your next instruction, or provide a path to an image or text file.
- The AI uses that input to continue working
- This loop repeats until:
  - You manually stop it, or
  - The session reaches your **tool call limit**

---

## 💡 Why This Matters

Most AI coding tools (like Cursor and Windsurf) offer **500 monthly requests**, but each request can include **up to 25 tool calls**. Normally, even saying `"hi"` uses up a full request, wasting potential.

With **CUTC**:
- You start with one request
- Within that session, you can give **multiple follow-ups**
- All follow-ups run within the same request using available tool calls
- This means you get **10x (or more)** actual work done with the same quota

---

## ⚙️ Ultra-Simple Installation

### Basic Installation (Auto-Detection)

```bash
python install.py
```

The installer will:
- 🔍 **Auto-detect** your IDE (Cursor or Windsurf)
- 📋 **Prompt** you to choose if both are detected
- 🚀 **Install** everything automatically

### Advanced Installation Options

```bash
# Install specifically for Cursor IDE
python install.py --ide cursor

# Install specifically for Windsurf IDE  
python install.py --ide windsurf

# Install for both IDEs
python install.py --ide both

# Keep installer for debugging
python install.py --keep-installer

# Get help
python install.py --help
```

**That's literally it!** 🎉

The installer:
- ✅ Contains all necessary files embedded within itself
- ✅ Auto-detects your IDE or prompts for selection
- ✅ Creates the proper IDE-specific structure
- ✅ Installs `userinput.py` at your project root
- ✅ Installs IDE-specific CUTC rules
- ✅ Self-destructs after successful installation
- ✅ Provides clear success/error messages
- ✅ Includes comprehensive troubleshooting

---

## 🧪 Project Structure

This is the **most minimalist** CUTC distribution possible:

```
CUTC/
├── install.py    # 🚀 Self-destructing all-in-one installer (10KB)
└── README.md     # 📖 Complete documentation (7KB)
```

After installation, your project will have:

### For Cursor IDE:
```
your-project/
├── .cursor/
│   └── rules/
│       └── cutc_rules.mdc     # 🤖 CUTC rules for Cursor
├── userinput.py               # 📝 User input script
└── [your existing files...]
```

### For Windsurf IDE:
```
your-project/
├── .windsurf/
│   └── rules/
│       └── cutc_rules.md      # 🌊 CUTC rules for Windsurf
├── userinput.py               # 📝 User input script
└── [your existing files...]
```

---

## 🆔 IDE-Specific Features

### 🎯 Cursor IDE Support
- **Structure**: `.cursor/rules/cutc_rules.mdc`
- **Format**: Markdown with YAML frontmatter
- **Mode**: Agent Mode
- **Features**: Full Cursor rules integration

### 🌊 Windsurf IDE Support  
- **Structure**: `.windsurf/rules/cutc_rules.md`
- **Format**: Pure Markdown
- **Mode**: Cascade Mode
- **Features**: Windsurf Cascade integration

### 🔄 Dual Installation
- **Auto-detection**: Intelligently detects existing IDE setups
- **Conflict resolution**: Handles projects with both IDEs
- **Unified experience**: Same functionality across both IDEs

---

## ⚠️ Important Note

**Only use this setup with tools that offer a tool call–based quota**, not token-based pricing (like OpenAI's pay-per-token). This setup is designed to **maximize bundled tool calls**, not minimize token usage.

---

## 🧠 Example

You have **500 monthly requests** and each request allows up to **25 tool calls**:

- **Normally:**
  `You say "hi" → AI replies "hi" = 1 request used.`

- **With CUTC:**
  `You say "hi" → AI replies → runs prompt → you say "add comments" → AI continues... (up to 25 calls)`
  = still **just 1 request used**, but you accomplished much more.

---

**Do more. Use fewer requests. Save your quota.**

**→ That's the power of CUTC.**

---

## 🔧 Troubleshooting

The installer includes built-in troubleshooting, but here are common solutions:

| Problem | Solution |
|---------|----------|
| **Rules don't apply** | Restart your IDE and check rules folder exists |
| **Permission denied** | Run as administrator (Windows) or with `sudo` (Linux/Mac) |
| **Python not found** | Install Python 3.6+ from [python.org](https://python.org) |
| **No terminal in chat** | Make sure you're in **Agent Mode** (Cursor) or **Cascade Mode** (Windsurf) |
| **IDE not detected** | Use `--ide cursor` or `--ide windsurf` flag |

---

## 🤝 Support and Contributions

### Original Support
Special thanks to [@perrypixel](https://github.com/perrypixel) for the original project:
- ☕ [Buy perrypixel a coffee](https://ko-fi.com/perrypixel)
- 💳 UPI: kevinp@apl

### CUTC Support
If you find CUTC useful, you can support the development:
- ☕ [Buy Thorrdu a coffee](https://ko-fi.com/thorrdu)
- 🐛 [Report bugs](https://github.com/Thorrdu/CUTC/issues)
- 💡 [Suggest improvements](https://github.com/Thorrdu/CUTC/discussions)

### Contributions
Contributions are welcome! Feel free to:
- Fork the project
- Create a feature branch
- Submit a Pull Request

---

## 🎯 Usage Tips

### For Cursor IDE:
1. **Start with Agent Mode**: Make sure Cursor is in Agent Mode
2. **Let it finish**: Allow the AI to complete each task fully
3. **Use the prompt**: When you see `prompt (or file path):`, you can:
    - Type your next instruction (e.g., `"add comments"`)
    - Drag and drop a file into the terminal to paste its path.
4. **Chain commands**: Keep adding tasks to maximize your tool calls
5. **Type 'stop'**: End the loop when you're done

### For Windsurf IDE:
1. **Start with Cascade Mode**: Make sure Windsurf is in Cascade Mode
2. **Let it finish**: Allow Cascade to complete each task fully
3. **Use the prompt**: When you see `prompt (or file path):`, you can:
    - Type your next instruction (e.g., `"refactor this"`)
    - Drag and drop a file into the terminal to paste its path.
4. **Chain commands**: Keep adding tasks to maximize your tool calls
5. **Type 'stop'**: End the loop when you're done

---

## 📄 License

This project inherits the license from the original project. See the original repository for more details.

---

## 🌟 Why CUTC is Better

- **🚀 Fastest setup**: One command, zero configuration
- **🖼️ Image & File Context**: Provide images and files as context
- **🎯 Dual IDE support**: Works with Cursor AND Windsurf
- **🔍 Smart detection**: Auto-detects your IDE setup
- **🗑️ Self-cleaning**: No leftover installation files
- **🛡️ Error-proof**: Smart error handling and recovery
- **📦 Minimal footprint**: Just 2 files total (17KB combined)
- **🔄 Always updated**: Embedded files ensure consistency
- **🌍 Cross-platform**: Works everywhere Python does
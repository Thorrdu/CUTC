# 🚀 Cursor Unlimited Tool Calls (CUTC)

**CUTC** is an ultra-minimalist tool designed for **Cursor IDE**, **Windsurf**, or any other agent-based coding assistant that supports tool calls. It helps you get the **maximum value from your monthly tool call allowance** by running your tasks in a loop with user input—without restarting the chat every time.

> **Important Note:** This only works with **Agent Mode**

---

## 🔄 Fork and Improvements

This project is an improved fork of the original [10x-Tool-Calls](https://github.com/perrypixel/10x-Tool-Calls) by [@perrypixel](https://github.com/perrypixel). 

**Huge thanks to perrypixel for the pioneering work!** 🙏

### 🎯 What we've improved:

- **Ultra-minimalist design**: Only 2 files in the entire project
- **Self-destructing installer**: Keeps your project clean after installation
- **Zero configuration**: One command does everything
- **Enhanced error handling**: Smart troubleshooting and recovery
- **Cross-platform support**: Works on Windows, Mac, and Linux

---

## ✅ What CUTC Does

- After the AI completes a task, it runs a small Python script that asks:

```
prompt: 
```

- You type your next instruction (e.g., `"add comments"`, `"refactor this"`, etc.)
- The AI uses that input to continue working
- This loop repeats until:
  - You manually stop it, or
  - The session reaches your **tool call limit**

---

## 💡 Why This Matters

Most AI coding tools (like Cursor) offer **500 monthly requests**, but each request can include **up to 25 tool calls**. Normally, even saying `"hi"` uses up a full request, wasting potential.

With **CUTC**:
- You start with one request
- Within that session, you can give **multiple follow-ups**
- All follow-ups run within the same request using available tool calls
- This means you get **10x (or more)** actual work done with the same quota

---

## ⚙️ Ultra-Simple Installation

### One Command Installation

```bash
python install.py
```

**That's literally it!** 🎉

The installer:
- ✅ Contains all necessary files embedded within itself
- ✅ Creates the proper `.cursor/rules/` structure
- ✅ Installs `userinput.py` at your project root
- ✅ Installs CUTC rules for Cursor IDE
- ✅ Self-destructs after successful installation
- ✅ Provides clear success/error messages
- ✅ Includes comprehensive troubleshooting

### Advanced Options

```bash
# Keep installer for debugging
python install.py --keep-installer

# Get help
python install.py --help
```

---

## 🧪 Project Structure

This is the **most minimalist** CUTC distribution possible:

```
CUTC/
├── install.py          # 🚀 Self-destructing installer (contains everything)
└── README.md          # 📖 This documentation
```

After installation, your project will have:
```
your-project/
├── .cursor/
│   └── rules/
│       └── cutc_rules.mdc     # 🤖 CUTC rules for Cursor
├── userinput.py               # 📝 User input script
└── [your existing files...]
```

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
| **Rules don't apply** | Restart Cursor IDE and check `.cursor/rules/` exists |
| **Permission denied** | Run as administrator (Windows) or with `sudo` (Linux/Mac) |
| **Python not found** | Install Python 3.6+ from [python.org](https://python.org) |
| **No terminal in chat** | Make sure you're in **Agent Mode** in Cursor |

---

## 🤝 Support and Contributions

### CUTC Support
If you find CUTC useful, you can support the development:
- ☕ [Buy Thorrdu a coffee](https://ko-fi.com/thorrdu)
- 🐛 [Report bugs](https://github.com/Thorrdu/CUTC/issues)
- 💡 [Suggest improvements](https://github.com/Thorrdu/CUTC/discussions)

### Original Support
Special thanks to [@perrypixel](https://github.com/perrypixel) for the original project:
- ☕ [Buy perrypixel a coffee](https://ko-fi.com/perrypixel)
- 💳 UPI: kevinp@apl

### Contributions
Contributions are welcome! Feel free to:
- Fork the project
- Create a feature branch
- Submit a Pull Request

---

## 🎯 Usage Tips

1. **Start with Agent Mode**: Make sure Cursor is in Agent Mode
2. **Let it finish**: Allow the AI to complete each task fully
3. **Use the prompt**: When you see `prompt:`, type your next instruction
4. **Chain commands**: Keep adding tasks to maximize your tool calls
5. **Type 'stop'**: End the loop when you're done

---

## 📄 License

This project inherits the license from the original project. See the original repository for more details.

---

## 🌟 Why CUTC is Better

- **🚀 Fastest setup**: One command, zero configuration
- **🗑️ Self-cleaning**: No leftover installation files
- **🛡️ Error-proof**: Smart error handling and recovery
- **📦 Minimal footprint**: Just 2 files total
- **🔄 Always updated**: Embedded files ensure consistency
- **🌍 Cross-platform**: Works everywhere Python does

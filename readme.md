# 🚀 Cursor Unlimited Tool Calls (CUTC)

**CUTC** is an ultra-simplified rules system designed for **Cursor IDE**, **Windsurf**, or any other agent-based coding assistant that supports tool calls. It helps you get the **maximum value from your monthly tool call allowance** by running your tasks in a loop with user input—without restarting the chat every time.

> **Important Note:** This only works with **Agent Mode**

---

## 🔄 Fork and Improvements

This project is an improved fork of the original [10x-Tool-Calls](https://github.com/perrypixel/10x-Tool-Calls) by [@perrypixel](https://github.com/perrypixel). 

**Huge thanks to perrypixel for the pioneering work!** 🙏

### 🎯 What we've improved:

- **Ultra-simplified installation**: One Python script does everything
- **Optimized file structure**: No more navigating through folders
- **Automatic installation**: No more manual manipulations
- **Better documentation**: Clearer instructions and troubleshooting

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

### Option 1: Automatic Installation (Recommended)

1. **Download** or clone this repository into your project
2. **Run** the installation script:

```bash
python install.py
```

3. **Restart** Cursor IDE
4. **Verify** that CUTC rules are active in settings

That's it! 🎉

### Option 2: Manual Installation

If you prefer to control each step:

1. **Copy** `cutc_rules.mdc` to `.cursor/rules/` in your project
2. **Copy** `userinput.py` to your project root
3. **Restart** Cursor IDE

---

## 🧪 Current Version

- ✅ **Supports:** text input only
- ✅ **Automatic installation** with Python script
- ✅ **Simplified structure** for rapid adoption
- ❌ **Not yet supported:** image upload or file drops (coming soon!)

A more advanced version is planned that will support:
- Image uploads
- File drops
- GUI installation interface

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

**Problem:** Rules don't apply
**Solution:** Check that the `.mdc` file is in `.cursor/rules/` and restart Cursor

**Problem:** Python script doesn't run
**Solution:** Verify that `userinput.py` is at the project root

**Problem:** Terminal doesn't open in chat
**Solution:** Make sure you're in Agent Mode in Cursor

---

## 🤝 Support and Contributions

### CUTC Support
If you find CUTC useful, you can support the development:
- ☕ [Buy Thorrdu a coffee](https://ko-fi.com/thorrdu)
- 🐛 [Report bugs](https://github.com/Thorrdu/cursor-10x-Tool-Calls/issues)
- 💡 [Suggest improvements](https://github.com/Thorrdu/cursor-10x-Tool-Calls/discussions)

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

## 📄 License

This project inherits the license from the original project. See the original repository for more details.

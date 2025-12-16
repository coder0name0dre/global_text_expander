# Global Text Expander

This script listens to your keyboard **system-wide** and replaces typed shortcuts (like ';addr' or ';date') with longer text after you press the Space.

**This works in any macOS application**

---

## Features

- Global keyboard listening (keyboard hooks)
- Expand text shortcuts in any app
- Dynamic expansions (e.g. current date)
- Safe handling of special keys
- Beginner friendly, single Python script
- Press **Esc** to exit cleanly

---

## Keyboard Hooks

Keyboard hooks allow the script to:

- Detect every key press globally
- Track recently typed characters
- Recognise shortcuts patterns
- Delete typed shortcuts
- Simulate typing replacement text

This project cannot work without keyboard hooks.

---


## Requirements

- macOS
- Python 3.9+
- `pynput` library

### Install dependencies:

```
pip install pynput
```

---

## macOS Permissions (IMPORTANT)

macOS blocks apps from monitoring keyboard input by default.

You **must** enable permission:

1. Open **System Settings**
2. Go to **Privacy & Security**
3. Click **Input Monitoring**
4. Enable:
  - **Terminal** (or the app running Python)
5. Restart Terminal
Without this permission, the script will not receive key events.

---


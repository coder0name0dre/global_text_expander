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

### Install Dependencies:

```
pip install pynput
```

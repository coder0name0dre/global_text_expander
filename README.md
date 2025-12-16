# Global Text Expander

This script listens to your keyboard **system-wide** and replaces typed shortcuts (like `;addr` or `;date`) with longer text after you press the Space.

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

## How To Run

1. Clone the repo:
```
git clone https://github.com/coder0name0dre/global_text_expander.git
cd global_text_expander
```

2. Run it:

```
python text_expander.py
```

You should see:

```
Text Expander running...
Try: ;addr, ;sig, ;email, ;date (then SPACE)
Press ESC to quit.
```

---

## How To Use

1. Open any application (Notes, browser, Mail, VS Code, etc.)
2. Type one of the shortcuts
3. Press Space
4. The shortcut is replaced automatically

### Example

Typing:

```
;date␣
```

Expands to(**e.g.**):

```
15-12-2025
```

---

## Default Shortcuts

| Shortcut        | Description |
|-----------------|-------------|
| ;addr           | Example address |
| ;sig            | Email signature |
| ;email          | Email address |
| ;date           | Current date (dynamic) |

---

## How To Exit

- Press **Esc**
- Or stop the script in Terminal using **Ctrl + C**

---

## Ethical & Safety

This script:
- Does not log keystokes
- Only reacts to predefined shortcuts
- Does not store or transmit input

Always use keyboard hooks responsibly.

Never capture passwords or sensitive personal data.

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/global_text_expander/blob/main/LICENSE).

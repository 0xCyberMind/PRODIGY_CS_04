# PRODIGY_CS_04
A simple Python keylogger using pynput to log keystrokes and save them in a file. It tracks alphanumeric and special keys, saving timestamps for each keypress. The logging session can be stopped by pressing the "Escape" key. Useful for monitoring key events on a device.
# Keylogger Python Script

This is a simple Python-based keylogger that logs every keystroke and saves it to a text file. The script tracks both alphanumeric and special keys, appending a timestamp for each keypress. The logging can be stopped by pressing the **Escape** key.

> **Warning**: Please use this script responsibly and ensure it is not used for unethical purposes.

---

## Features

- **Keystroke Logging**: Captures every key pressed on the keyboard.
- **Timestamping**: Each keystroke is logged with its timestamp.
- **Special Key Detection**: Tracks special keys like Shift, Ctrl, Space, etc.
- **Logging Control**: Press the **Escape** key to stop logging.
- **Log File**: Logs are saved to `keylog.txt` in the same directory.

---

## Prerequisites

Before running the script, make sure you have:

- **Python 3.x** installed on your system.
- The **`pynput` library**: This script uses the `pynput` library to capture keyboard events. You can install it via pip:

    ```bash
    pip install pynput
    ```

---

## Installation and Usage

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
https://github.com/0xCyberMind/PRODIGY_CS_04.git
```


### 2. Run the Script
```bash
python task_04.py
```
### 3. Logging Keystrokes

Once the script is running, every keypress you make will be logged in a file named keylog.txt. The log will include the key pressed and a timestamp for each keypress.

### 4. Stopping the Logging

To stop logging, press the Escape key. The script will stop recording and write a final entry to indicate that logging has been stopped. The program will then exit.

### Example of Log File

The keylog.txt file will look something like this:

```bash
--- Logging Started: 2025-08-30 14:12:05.234000 ---
2025-08-30 14:12:10: Key 'a' pressed
2025-08-30 14:12:11: Key 'b' pressed
2025-08-30 14:12:13: Special Key 'shift' pressed
2025-08-30 14:12:15: Key ' ' pressed
2025-08-30 14:12:17: Special Key 'esc' pressed
--- Logging Stopped by user (esc): 2025-08-30 14:12:18 ---

```
### Disclaimer

This script is for educational purposes only. Unauthorized monitoring or recording of user activity without consent is illegal and unethical. Make sure you have explicit permission before running such scripts on any system.

### Author

Name: 0xcybermind

GitHub: 0xcybermind

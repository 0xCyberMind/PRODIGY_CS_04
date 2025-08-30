# PRODIGY_CS_04
A simple Python keylogger using pynput to log keystrokes and save them in a file. It tracks alphanumeric and special keys, saving timestamps for each keypress. The logging session can be stopped by pressing the "Escape" key. Useful for monitoring key events on a device.
# Keylogger Python Script

This is a simple Python-based keylogger that logs every keystroke and saves it to a text file. The script tracks both alphanumeric and special keys, appending a timestamp for each keypress. The logging can be stopped by pressing the **Escape** key. 

> **Warning**: Please use this script responsibly and ensure it is not used for unethical purposes.

## Features

- **Keystroke Logging**: Captures every key pressed on the keyboard.
- **Timestamping**: Each keystroke is logged with its timestamp.
- **Special Key Detection**: Tracks special keys like Shift, Ctrl, Space, etc.
- **Logging Control**: Press the **Escape** key to stop logging.
  
## Usage

### Prerequisites

You need Python 3.x and the `pynput` library to run the script. If you don’t have `pynput` installed, you can install it via `pip`:

```bash
pip install pynput
Running the Script
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/keylogger-python.git
Navigate to the project directory:

bash
Copy code
cd keylogger-python
Run the script:

bash
Copy code
python keylogger.py
Every keypress will be logged in a file named keylog.txt. When you press the Escape key, logging will stop.

Example of Log File
txt
Copy code
--- Logging Started: 2025-08-30 14:12:05.234000 ---
2025-08-30 14:12:10: Key 'a' pressed
2025-08-30 14:12:11: Key 'b' pressed
2025-08-30 14:12:13: Special Key 'shift' pressed
2025-08-30 14:12:15: Key ' ' pressed
2025-08-30 14:12:17: Special Key 'esc' pressed
--- Logging Stopped by user (esc): 2025-08-30 14:12:18 ---
File Output
Keylog File: All logged keys are stored in the keylog.txt file.

Timestamp: Each log entry has a timestamp marking when the key was pressed.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
This script is for educational purposes only. Unauthorized monitoring or recording of user activity without consent is illegal and unethical. Make sure you have permission before running such scripts on any system.

Author
Your Name

yaml
Copy code

---

### Description Breakdown:

1. **Repository Description**: The short explanation (less than 350 characters) succinctly describes the functionality of the script.
2. **`README.md`**: The readme provides detailed information on what the script does, how to use it, what dependencies are required, and examples of how it works. It includes clear instructions for setting up the environment, running the script, and reviewing the output.
3. **Ethical Disclaimer**: It's important to add a note about using the script responsibly to avoid misuse, especially since keyloggers can be seen as potentially harmful or invasive.

Let me know if you need further adjustments!

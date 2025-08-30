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
Every keypress will be logged in a file named keylog.txt. When you press the Escape key, logging will stop.!--




# Keylogger
Keylogger Script This repository contains a simple keylogger script written in Python. The keylogger captures keystrokes and periodically sends them to a specified server.
## Features
**📋 Captures all keystrokes including special keys (e.g., space, enter).**

**🌐 Logs are sent to a remote server at specified intervals.**

**⚙️ User is prompted to input the server's IP address and port number.**

**🖥️ Designed to run seamlessly in the background.**
# Requirements
**Python 3.x**

**pynput library**
# 🚀 Installation

## 1.Clone the repository:

``` https://github.com/Dxvan06/Keylogger.git ```

``` cd ```

## 2.Install the required library:

``` pip install pynput ```

## 3.Make the script executable (if on Linux/macOS):

``` chmod +x attacker.py ```

``` chmod +x victime.py ```

# 🏃‍♂️ Usage

1.Run the server script on the attacker machine:

``` ./attacker.py ```

This will start the server that receives the logs.

2.Run the keylogger script on the victim machine:

``` ./victime.py ```

**Note: Enter the attacker machine IP and PORT number in the ``` victime.py ``` script.**

# 🪟 Creating Windows Executables

To create Windows executables for both scripts, use pyinstaller:

## 1.Install PyInstaller:

``` pip install pyinstaller  ```

## 2.Create executables:

``` pyinstaller --onefile victime.py ```

 *The executables will be created in the ``dist`` folder.* 

# ⚠️ Disclaimer
This script is intended for educational purposes only. Unauthorized use of this script is prohibited and may be illegal. The author is not responsible for any misuse or damage caused by this script.





